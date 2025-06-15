from PySide6.QtCore import QObject

from .model import AppModel
from .view import AppView
from .backend.consts import *

class AppController(QObject):
    def __init__(self, model:AppModel, view:AppView):
        super().__init__()
        self.__model = model
        self.__view = view

        self.__loginForm = loginForm = view.loginForm()
        self.__loadingForm = view.loadingForm()

        # conectando eventos
        loginForm.continueRequired.connect(self.on_loginForm_continueRequired)
        model.initializationFinished.connect(self.on_model_initializationFinished)
        

    def initialize(self):
        self.__view.initialize()
        self.__view.setupUiById(UI_ID_LOADING)
        self.__loadingForm.setText('inicializando componentes...')

        self.__model.initialize()

    def on_loginForm_continueRequired(self):
        self.login(*self.__loginForm.getEntries())

        

    def on_model_initializationFinished(self, success:bool):
        if not success:
            self.__loadingForm.setText('não foi possível inicializar os componentes')
            return

        credentials = self.__model.getCachedCredentials()

        if self.__model.rememberCredentials() and credentials:
            self.login(*credentials, setupLogin=True)
            return
        
        self.__view.setupUiById(UI_ID_LOGIN)

    def login(self, username:str, password:str, remember:bool=False, setupLogin=False):
        if not (username and password):
            self.__view.showMessage('Preencha todos os campos!', 5000)

            if setupLogin:
                self.__view.setupUiById(UI_ID_LOGIN)

            return
        
        if not self.__model.login(username, password, remember):
            self.__view.showMessage('Usuário ou senha incorretos!', 5000)

            if setupLogin:
                self.__view.setupUiById(UI_ID_LOGIN)

            return
        
        self.__view.setupUiById(UI_ID_MAIN)
        self.__view.mainForm().setUsername(self.__model.getUserFullname())