from PySide6.QtCore import QObject
import logging
from configparser import ConfigParser
import os

from .. import api as api
from ..api.structs import Registry
from ..backend._events import EventHandlerApp
from ..backend._consts import *
from ..backend import _tools as tools

class ModelApp(QObject):
    def __init__(self, parent:QObject):
        super().__init__(parent, objectName='ModelApp')
        self.__eventHandler = EventHandlerApp(self)
        self.__events = self.__eventHandler.model
        self.__api = api.FinanceiroAPI(os.environ.get('DATABASE_ENGINE', 'sqlite3'))
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
        
        self.__config.read('config.ini')
        if 'Login' not in self.__config:
            self.__rememberCredentials(False) # gerando valores-padrão para objeto config

        self.events.initializationFinished.emit(self.__api.connect('database.db'))
    
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
    
    def getRegistriesToTable(self) -> tuple[list[Registry], list[list[str]]]:
        """
        consulta os registros e retorna estruturado para exibição na tabela
        
        retorno: registries, values
        """
        values = []
        banks = {}
        cards = {}
        regs = self.api.getAllRegistries()

        for reg in regs:
            if reg.type == api.consts.REG_TYPE_IN:
                _type = 'Entrada'
            
            elif reg.type == api.consts.REG_TYPE_OUT:
                _type = 'Saída'

            else:
                raise ValueError('tipo de registro desconhecido')

            if reg.bank_id not in banks and reg.bank_id is not None:
                banks[reg.bank_id] = self.api.getBank(reg.bank_id).name

            if reg.card_id not in banks and reg.card_id is not None:
                cards[reg.card_id] = str(self.api.getCard(reg.card_id).num).zfill(4)
            
            str_dt = reg.datetime.strftime('%H:%M %d/%m/%Y')
            desc = reg.description if reg.description else '-'
            bank_name = banks.get(reg.bank_id, '-')
            v_int, v_decimal = str(reg.value).split('.')
            str_value = f'R$: {v_int},{v_decimal.ljust(2, '0')}'
            card = cards.get(reg.card_id, '-')
            
            values.append([reg.title, _type, str_value, str_dt, desc, bank_name, card])

        return regs, values

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