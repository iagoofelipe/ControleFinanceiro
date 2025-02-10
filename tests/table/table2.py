# pyside6-uic financeiroapp\ui\src\Table.ui -o tests\table\ui_table.py

from PySide6.QtWidgets import QWidget, QTableWidgetItem, QApplication, QMainWindow
from PySide6.QtCore import Signal
from PySide6.QtGui import QGuiApplication
from PySide6.QtCore import Qt
from typing import Iterable, Sequence

from ui_table import Ui_Table

# Ui Components - Table
TABLE_HEADER_TITLE = 1
TABLE_HEADER_BTN_EDIT = 2
TABLE_HEADER_BTN_CONFIRM = 3
TABLE_HEADER_BTN_DELETE = 4
TABLE_HEADER_ALL_BTNS = 5

def getNavigationInfo(length:int, limit:int, index:int) -> tuple[int, int, int, int, int]:
    """
    calcula os valores inicial, final e número de intervalos a partir das informações de length, limit e index.
    Realiza o tratamento de limit e index de acordo com length
    
    retorna start, end, limit, index, num_intervals
    """

    if not (0 < limit < length):
        limit = length

    num_intervals = (length // limit) + (length % limit != 0)

    if length == 0:
        return 0, 0, 0, num_intervals
    
    if index >= num_intervals:
        index = num_intervals - 1

    start = index * limit + 1 # just works if length is bigger than one
    end = (index + 1) * limit if (index + 1 < num_intervals) else length

    return start, end, limit, index, num_intervals

class Table(QWidget):
    confirmRequired = Signal()
    editRequired = Signal()
    deleteRequired = Signal()

    def __init__(self, parent:QWidget, *, title:str=None, flags:set[int] = None):
        super().__init__(parent)
        self.__ui = Ui_Table()
        self.__title = title
        flags = flags if flags is not None else set()
            
        if title is not None:
            flags.add(TABLE_HEADER_TITLE)

        self.__ui.setupUi(self)

        # conectando eventos
        self.__ui.btnPrv.clicked.connect(lambda: self.setGroupValuesByIndex(self.__index-1))
        self.__ui.btnNext.clicked.connect(lambda: self.setGroupValuesByIndex(self.__index+1))
        self.__ui.tableWidget.itemSelectionChanged.connect(self.on_tableWidget_itemSelectionChanged)

        self.setFlags(flags)

    def on_tableWidget_itemSelectionChanged(self):
        rows = set([item.row() for item in self.__ui.tableWidget.selectedItems()])
        num_selections = len(rows)

        # configurando botões de acordo com a quantidade de itens selecionados
        if not rows: # == 0
            confirm = False
            edit = False
            delete = False
        
        elif num_selections == 1:
            confirm = True
            edit = True
            delete = True

        else: # > 1
            confirm = True
            edit = False
            delete = True

        self.__ui.btnConfirm.setEnabled(confirm)
        self.__ui.btnEdit.setEnabled(edit)
        self.__ui.btnDelete.setEnabled(delete)

    def reset(self):
        self.__ui.tableWidget.setRowCount(0)
        self.__ui.tableWidget.setColumnCount(0)

        self.__ui.widHeader.hide()
        self.__ui.labelTitle.hide()
        self.__ui.btnConfirm.hide()
        self.__ui.btnEdit.hide()
        self.__ui.btnDelete.hide()
        self.__ui.line.hide()
        self.__ui.tableWidget.clear()
        self.__ui.label.clear()

        for btnName in ('Confirm', 'Edit', 'Delete', 'Prv', 'Next'):
            self.__ui.__getattribute__('btn'+btnName).setDisabled(True)

    def setValues(self, values:Iterable[Iterable], headers:Sequence[str], limit=-1):
        self.__values = values
        self.__len = len(values)
        self.__limit = limit
        
        self.__ui.tableWidget.clear()
        self.__ui.tableWidget.setColumnCount(len(headers))
        self.__ui.tableWidget.setHorizontalHeaderLabels(headers)

        self.setGroupValuesByIndex(0)
    
    def setGroupValuesByIndex(self, index:int):
        if not self.__len: # caso não hajam valores
            self.__ui.btnPrv.setDisabled(True)
            self.__ui.btnNext.setDisabled(True)
            self.__ui.label.setText('')
            return

        start, end, _, self.__index, num_intervals = getNavigationInfo(self.__len, self.__limit, index)
        num_interval = self.__index + 1
        hasPrv = num_interval > 1
        hasNext = num_interval < num_intervals
        values = self.__values[start-1:end]

        # populando tabela
        self.__ui.tableWidget.setRowCount(len(values))
        index_row_general = start
        for index_row, row in enumerate(values):
            self.__ui.tableWidget.setVerticalHeaderItem(index_row, QTableWidgetItem(str(index_row_general)))
            index_row_general += 1

            for index_col, v in enumerate(row):
                item = QTableWidgetItem(str(v))
                self.__ui.tableWidget.setItem(index_row, index_col, item)

        self.__ui.btnPrv.setEnabled(hasPrv)
        self.__ui.btnNext.setEnabled(hasNext)
        self.__ui.label.setText(f'{start} a {end} de {self.__len}')

    def setTitle(self, title:str):
        self.__ui.line.show()
        self.__ui.labelTitle.show()
        self.__ui.labelTitle.setText(title)
        self.__flags.add(TABLE_HEADER_TITLE)

    def setFlags(self, flags:set[int]):
        self.__flags = flags
        self.reset()

        if TABLE_HEADER_BTN_CONFIRM in flags or TABLE_HEADER_ALL_BTNS in flags:
            self.__ui.btnConfirm.show()

        if TABLE_HEADER_BTN_EDIT in flags or TABLE_HEADER_ALL_BTNS in flags:
            self.__ui.btnEdit.show()

        if TABLE_HEADER_BTN_DELETE in flags or TABLE_HEADER_ALL_BTNS in flags:
            self.__ui.btnDelete.show()

        if TABLE_HEADER_TITLE in flags:
            self.setTitle(self.__title)

        if flags:
            self.__ui.widHeader.show()




if __name__ == '__main__':
    app = QApplication()
    window = QMainWindow()
    table = Table(None, flags={TABLE_HEADER_ALL_BTNS})
    headers = ['valor', 'atendente', 'produto']
    values = [
        [11.4, 'iago', 'produto 1'],
        [22.4, 'iago', 'produto 2'],
        [5.5, 'marcos', 'produto 3'],
        [4.1, 'carlos', 'produto 4'],
        [3, 'carlos', 'produto 5'],
        [3, 'josé', 'produto 5'],
        [3.4, 'iago', 'produto 6'],
        [3.9, 'marcos', 'produto 7'],
    ]

    table.setValues(values, headers, 5)    
    QGuiApplication.styleHints().setColorScheme(Qt.ColorScheme.Light)
    window.setCentralWidget(table)
    window.show()
    app.exec()
