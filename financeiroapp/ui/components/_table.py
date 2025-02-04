from PySide6.QtWidgets import QWidget
from typing import Iterable

from ..auto.ui_table import Ui_Table 
from ...backend._consts import *

class Table(QWidget):
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

    def setTitle(self, title:str):
        self.__ui.labelTitle.setText(title)

    def setFlags(self, flags:set[int]):
        hasHeader = False
        hasTitle = TABLE_HEADER_TITLE in flags

        if TABLE_HEADER_EDIT in flags:
            hasHeader = True
            self.__ui.btnEdit.show()

        if TABLE_HEADER_CONFIRM in flags:
            hasHeader = True
            self.__ui.btnConfirm.show()

        if TABLE_HEADER_DELETE in flags:
            hasHeader = True
            self.__ui.btnDelete.show()

        if hasTitle:
            hasHeader = True
            self.setTitle(self.__title)

        self.__ui.line.setVisible(hasTitle)
        self.__ui.labelTitle.setVisible(hasTitle)
        self.__ui.widHeader.setVisible(hasHeader)