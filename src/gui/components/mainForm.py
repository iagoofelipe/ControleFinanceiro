from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QWidget

from .abstractForm import AbstractForm
from ..generated.MainForm import Ui_MainForm
from ...backend.consts import UI_ID_MAIN

class MainForm(AbstractForm):
    ID = UI_ID_MAIN

    logoutRequired = Signal()

    def __init__(self, parent:QObject=None):
        super().__init__(parent)
        self.__ui = Ui_MainForm()

    def setup(self, parent:QWidget=None):
        self.__wid = wid = QWidget(parent)

        # configurando componentes
        self.__ui.setupUi(wid)
        self.__ui.btnSair.clicked.connect(self.logoutRequired)

        return wid
    
    def setUsername(self, text:str):
        self.__ui.labelUsername.setText('Bem-vindo, %s!' % text)