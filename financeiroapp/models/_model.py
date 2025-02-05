from PySide6.QtCore import QObject
from threading import Thread
import logging
from configparser import ConfigParser

# MySQL
from mysql.connector import connect
from mysql.connector.errors import ProgrammingError
from mysql.connector import MySQLConnection
from mysql.connector.cursor import MySQLCursor

from ..backend._events import EventHandlerApp
from ..backend._consts import *
from ..backend import _tools as tools

class ModelApp(QObject):
    __conn:MySQLConnection = None
    __cursor:MySQLCursor = None
    __config:ConfigParser = None
    __connParams = {
            'host': DATABASE_HOST,
            'user': DATABASE_USER,
            'password': DATABASE_PASSWORD,
            'database': DATABASE_SCHEMA,
        }

    def __init__(self, parent:QObject):
        super().__init__(parent, objectName='ModelApp')
        self.__eventHandler = EventHandlerApp(self)
        self.__events = self.__eventHandler.model
        self.__userId = None
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

    # -----------------------------------------------------------------
    # Métodos Públicos
    def initialize(self):
        self.logger.debug(f'ModelApp::initialize')
        self.events.initializationStarted.emit()

        def func():
            success = True
            self.__config = ConfigParser()
            self.__config.read('config.ini')

            if 'Login' not in self.__config:
                self.__rememberCredentials(False)

            try:
                self.__conn = connect(**self.__connParams)
                self.__cursor = self.__conn.cursor()

            except ProgrammingError:
                self.__conn = None
                success = False

            self.events.initializationFinished.emit(success)

        Thread(target=func).start()
    
    def login(self, username:str, password:str, remember:bool):
        self.events.loginRequired.emit(username, password, remember)
        self.logger.debug(f'ModelApp::login <username={username}, password={password}, remember={remember}>')
        
        if not self.__conn.is_connected():
            self.events.loginFinished.emit(False)
            return
        
        self.__cursor.execute('SELECT id FROM user WHERE username=%s AND password=%s', (username, password))
        r = self.__cursor.fetchone()
        success = r is not None

        if success:
            self.__rememberCredentials(remember, username, password)

        self.__userId = r[0] if success else None
        self.events.loginFinished.emit(success)
                
    def getCurrentUserName(self) -> str | None:
        if self.__userId is None or not self.__conn.is_connected():
            return
        
        self.__cursor.execute('SELECT first_name, last_name FROM user WHERE id=%s', (self.__userId, ))
        r = self.__cursor.fetchone()
        if r is None:
            raise ValueError('invalid userId')
        
        return ' '.join(r)
    
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