from PySide6.QtCore import QObject
from PySide6.QtWidgets import QMainWindow

from .model import AppModel
from .gui.components.loginForm import LoginForm
from .gui.components.mainForm import MainForm
from .gui.components.loadingForm import LoadingForm

class AppView(QObject):
    def __init__(self, model:AppModel):
        super().__init__()
        self.__model = model
        self.__window = QMainWindow()
        self.__loginForm = LoginForm(self)
        self.__mainForm = MainForm(self)
        self.__loadingForm = LoadingForm(self)

        self.__statusBar = self.__window.statusBar() # força a criação da barra de status

    def initialize(self):
        self.__window.resize(700, 600)
        self.__window.setWindowTitle('Controle Financeiro')
        self.__window.show()

    def showMessage(self, text:str, timeout:int|None=None):
        self.__statusBar.showMessage(text, timeout)

    def setupUiById(self, id:int):
        ui = None

        match id:
            case LoginForm.ID:
                ui = self.__loginForm

            case MainForm.ID:
                ui = self.__mainForm

            case LoadingForm.ID:
                ui = self.__loadingForm

            case _:
                raise ValueError(f'undefined ui with id {id}')
            
        self.__window.setCentralWidget(ui.setup())

    def loginForm(self): return self.__loginForm
    def mainForm(self): return self.__mainForm
    def loadingForm(self): return self.__loadingForm

    