from PySide6.QtCore import QObject, Signal
from mysql.connector import connect
from threading import Thread
from configparser import ConfigParser

from .backend.consts import SETTINGS_FILE

class AppModel(QObject):
    initializationFinished = Signal(bool)

    def __init__(self):
        super().__init__()
        self.__user_id = None
        self.__user_fullname = None
        self.__config = ConfigParser()

    def initialize(self):
        Thread(target=self.__initialize).start()

    def __initialize(self):
        self.__config.read(SETTINGS_FILE)
        try:
            self.__con = connect(host='localhost', username='test', password='1234', database='financeiro')
            self.__cursor = self.__con.cursor()

        except Exception as e:
            self.__con = None
            print(f'[AppModel::initialize] error {e}')

        success = bool(self.__con)
        print(f'[AppModel::initialize] success {success}')
        self.initializationFinished.emit(success)

    def login(self, username:str, password:str, remember=False) -> bool:
        self.__cursor.execute('SELECT id, fullname FROM usuario WHERE username=%s AND password=%s', (username, password))
        data = self.__cursor.fetchone()

        if not data:
            return False

        self.__user_id, self.__user_fullname = data
        
        if remember:
            self.saveCredentials(username, password)
        else:
            self.clearCachedCredentials()

        return True
    
    def getUserFullname(self) -> str: return self.__user_fullname
    
    def rememberCredentials(self) -> bool:
        try:
            return self.__config['Credentials'].getboolean('remember')
        except:
            return False

    def getCachedCredentials(self) -> tuple[str, str] | None:
        if not self.__config.has_section('Credentials') or 'username' not in self.__config['Credentials'] or 'password' not in self.__config['Credentials']:
            return
        
        section = self.__config['Credentials']

        return section['username'], section['password']
    
    def saveCredentials(self, username:str, password:str):
        if not self.__config.has_section('Credentials'):
            self.__config.add_section('Credentials')
        
        section = self.__config['Credentials']

        if (
            'username' in section and section['username'] == username \
            and 'password' in section and section['password'] == password \
            and 'remember' in section and section['remember'] == 'True' \
            ):
            return

        print('[AppModel::saveCredentials] updating file...')
        section['username'] = username
        section['password'] = password
        section['remember'] = 'True'

        with open(SETTINGS_FILE, 'w') as f:
            self.__config.write(f)

    def clearCachedCredentials(self):
        self.__config.remove_section('Credentials')

        with open(SETTINGS_FILE, 'w') as f:
            self.__config.write(f)