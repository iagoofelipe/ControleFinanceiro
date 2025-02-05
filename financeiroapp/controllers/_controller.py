from PySide6.QtCore import QObject

from ..models._model import ModelApp
from ..views._view import ViewApp
from ..backend._consts import *
from ..backend import _tools as tools

class ControllerApp(QObject):
    def __init__(self, parent:QObject):
        super().__init__(parent, objectName='ControllerApp')
        self.__model = ModelApp(self)
        self.__view = ViewApp(self, self.__model)
        self.__events = self.__model.eventHandler.controller

        # conectando eventos
        self.model.events.initializationFinished.connect(self.on_model_initializationFinished)
        self.model.events.loginFinished.connect(self.on_model_loginFinished)

    # -----------------------------------------------------------------
    # Propriedades
    @property
    def view(self):
        return self.__view
    
    @property
    def model(self):
        return self.__model
    
    @property
    def events(self):
        return self.__events
    
    # -----------------------------------------------------------------
    # Métodos Públicos
    def initialize(self):
        self.model.logger.debug(f'ControllerApp::initialize')
        self.events.initializationStarted.emit()
        self.view.initialize()
        self.model.initialize()
        # continua após finalizar em on_model_initializationFinished
        
    # -----------------------------------------------------------------
    # Slots
    def on_model_initializationFinished(self, success:bool):
        self.model.logger.debug(f'ControllerApp::on_model_initializationFinished <success={success}>')
        
        self.events.initializationFinished.emit()
        if success:
            if self.model.config.getboolean('Login', 'remember'):
                username = self.model.getRememberUsername()
                password = self.model.getRememberPassword()
                remember = username and password

                self.model.login(username, password, remember)
                return

            self.view.setupPageById(PAGE_ID_LOGIN)
            return
        
        pageLoading = self.view.getPageById(PAGE_ID_LOADING)
        pageLoading.setMessage('não foi possível realizar a conexão com o servidor')

    def on_model_loginFinished(self, success:bool):
        self.model.logger.debug(f'ControllerApp::on_model_loginFinished <success={success}>')

        if success:
            self.view.setupPageById(PAGE_ID_REG)
            print(f'Olá, {self.model.getCurrentUserName()}!')

        elif not self.view.checkCurrentPageById(PAGE_ID_LOGIN): # caso a página atual não seja de login
            self.view.setupPageById(PAGE_ID_LOGIN)