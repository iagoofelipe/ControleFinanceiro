from PySide6.QtCore import QObject
from threading import Thread
import logging
from configparser import ConfigParser

from .. import api
from ..backend._events import EventHandlerApp
from ..backend._consts import *
from ..backend import _tools as tools

class ModelApp(QObject):
    def __init__(self, parent:QObject):
        super().__init__(parent, objectName='ModelApp')
        self.__eventHandler = EventHandlerApp(self)
        self.__events = self.__eventHandler.model
        self.__api = api.FinanceiroAPI()
        self.__config = ConfigParser()
        self.__logger = logging.getLogger('FinanceiroApp')
        logging.basicConfig(level=logging.DEBUG, format='[%(asctime)s %(levelname)s::%(name)s] %(message)s', datefmt='%H:%M:%S')

    # -----------------------------------------------------------------
    # Propriedades
    @property
    def events(self):
        return self.__events
    
    @property
    def eventHandler(self):
        return self.__eventHandler
    
    @property
    def logger(self):
        return self.__logger
    
    @property
    def config(self):
        return self.__config
    
    @property
    def api(self):
        return self.__api

    # -----------------------------------------------------------------
    # Métodos Públicos
    def initialize(self):
        self.logger.debug(f'ModelApp::initialize')
        self.events.initializationStarted.emit()

        def func():
            self.__config.read('config.ini')

            if 'Login' not in self.__config:
                self.__rememberCredentials(False) # gerando valores-padrão para objeto config

            self.events.initializationFinished.emit(self.__api.connect(DATABASE_PARAMS))

        Thread(target=func).start()
    
    def login(self, username:str, password:str, remember:bool):
        self.events.loginRequired.emit(username, password, remember)
        self.logger.debug(f'ModelApp::login <username={username}, password={password}, remember={remember}>')
        
        if not self.__api.isConnected():
            self.events.loginFinished.emit(False)
            return
        
        success = self.__api.login(username, password)

        self.__rememberCredentials(success and remember, username, password)
        self.events.loginFinished.emit(success)
                
    def getCurrentUserName(self) -> str | None:
        if not self.__api.isLogged():
            return
        
        user = self.__api.getCurrentUser()
        return user.first_name + ' ' + user.last_name

    def getRememberUsername(self) -> str:
        username = tools.decrypt(self.config.get('Login', 'username'))
        return username if username else ''
    
    def getRememberPassword(self) -> str:
        password = tools.decrypt(self.config.get('Login', 'password'))
        return password if password else ''


    # -----------------------------------------------------------------
    # Métodos Privados
    def __rememberCredentials(self, remember:bool, username:str='', password:str=''):
        val = {
                'Login': {
                    'username': tools.encrypt(username), 
                    'password': tools.encrypt(password), 
                    'remember': True,
                }
            } if remember else {
                'Login': {
                    'username': '', 
                    'password': '', 
                    'remember': False,
                }
            }

        self.__config.update(val)

        with open(CONFIG_FILE, 'w') as f:
            self.__config.write(f)