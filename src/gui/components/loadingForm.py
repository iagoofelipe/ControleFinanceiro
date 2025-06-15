from PySide6.QtWidgets import QWidget, QLabel
from PySide6.QtCore import Qt

from .abstractForm import AbstractForm
from ...backend.consts import UI_ID_LOADING

class LoadingForm(AbstractForm):
    ID = UI_ID_LOADING

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__label = None

    def setup(self, parent=None):
        self.__wid = self.__label = QLabel('...', parent, alignment=Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignHCenter)

        return self.__wid
    
    def setText(self, text:str):
        self.__label.setText(text)