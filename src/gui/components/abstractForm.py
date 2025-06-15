from PySide6.QtCore import QObject
from PySide6.QtWidgets import QWidget

class AbstractForm(QObject):
    __wid:QWidget | None = None
    ID:int = None

    def __init__(self, parent:QObject=None):
        super().__init__(parent)

    def widget(self): return self.__wid

    def setup(self, parent:QWidget=None) -> QWidget: ...