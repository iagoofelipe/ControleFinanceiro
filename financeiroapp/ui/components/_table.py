from PySide6.QtWidgets import QWidget, QTableWidgetItem
from PySide6.QtCore import Signal
from typing import Iterable, Sequence

from ..auto.ui_table import Ui_Table 
from ...backend._consts import *
from ...backend._tools import getNavigationInfo

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

    #------------------------------------------------------------------------------------
    # Métodos Públicos
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
        self.__ui.tableWidget.resizeColumnsToContents()

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

    #------------------------------------------------------------------------------------
    # Eventos
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