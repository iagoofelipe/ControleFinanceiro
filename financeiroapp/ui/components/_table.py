from PySide6.QtWidgets import QWidget, QTableWidgetItem
from PySide6.QtCore import Signal
from typing import Iterable, Any

from ..auto.ui_table import Ui_Table 
from ...backend._consts import *

class Table(QWidget):
    confirmRequired = Signal()
    editRequired = Signal()
    deleteRequired = Signal()
    previousRequired = Signal()
    nextRequired = Signal()

    def __init__(self, parent:QWidget, *, title:str=None, flags:set[int] = None):
        super().__init__(parent)
        self.__ui = Ui_Table()
        self.__title = title
            
        if title and flags is not None:
            flags.add(TABLE_HEADER_TITLE)

        self.__ui.setupUi(self)
        self.__ui.btnConfirm.hide()
        self.__ui.btnEdit.hide()
        self.__ui.btnDelete.hide()

        if flags:
            self.setFlags(flags)

    def setQuantityTitle(self, init:int, end:int, total:int):
        self.__ui.label.setText(f'{init} a {end} de {total}')

    def setValues(self, values:Iterable[dict[str, Any]], limit=5):
        self.__values = values
        len_values = len(values)
        show_all = len_values <= limit
        end = limit if not show_all else len_values

        # configurando navegabilidade
        self.__ui.btnPrv.setDisabled(True)
        self.__ui.btnNext.setDisabled(show_all)

        if not values:
            self.setQuantityTitle(0, 0, 0)
            return
        
        self.setQuantityTitle(1, end, len_values)
        # self.__ui.tableWidget.

    def setTitle(self, title:str):
        self.__ui.labelTitle.setText(title)

    def setFlags(self, flags:set[int]):
        hasHeader = False
        hasTitle = TABLE_HEADER_TITLE in flags

        if TABLE_HEADER_CONFIRM in flags:
            hasHeader = True
            self.__ui.btnConfirm.show()

        if TABLE_HEADER_EDIT in flags:
            hasHeader = True
            self.__ui.btnEdit.show()

        if TABLE_HEADER_DELETE in flags:
            hasHeader = True
            self.__ui.btnDelete.show()

        if hasTitle:
            hasHeader = True
            self.setTitle(self.__title)

        self.__ui.line.setVisible(hasTitle)
        self.__ui.labelTitle.setVisible(hasTitle)
        self.__ui.widHeader.setVisible(hasHeader)