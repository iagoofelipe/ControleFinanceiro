# from mysql.connector import connect
# from mysql.connector.errors import ProgrammingError
import sqlite3
from .structs import *
from .consts import *
from .errors import *
from . import tools

class FinanceiroAPI:
    def __init__(self, db_engine):
        self.__conn = None
        self.__cursor = None
        self.__currentUser = None

        match db_engine:
            case 'sqlite3':
                self.__param = '?'
            
            case 'mysql':
                self.__param = '%s'

    # -----------------------------------------------
    #region Métodos Públicos
    def isLogged(self):
        return self.__currentUser is not None

    def isConnected(self):
        return self.__conn is not None
    
    def login(self, username, password):
        self.__checkConnection()
        
        self.__cursor.execute(f'SELECT id FROM user WHERE username={self.__param} AND password={self.__param}', (username, password))
        r = self.__cursor.fetchone()

        if r is None:
            self.__currentUser = None
            return False
        
        self.__currentUser = self.getUser(r[0])
        return True
    
    def connect(self, filename):
        try:
            self.__conn = sqlite3.connect(filename)

        except:
            self.__conn = None
            self.__cursor = None
            return False

        self.__cursor = self.__conn.cursor()
        return True

    def checkCredentials(self, username, password):
        self.__checkConnection()
        
        self.__cursor.execute(f'SELECT id FROM user WHERE username={self.__param} AND password={self.__param}', (username, password))
        return self.__cursor.fetchone() is not None

    def updateObject(self, instance_of_obj):
        obj = instance_of_obj
        self.__checkSubclass(type(obj))
        
        str_keyParam = ', '.join(map(lambda x: f'`{x}`={self.__param}', obj.COLUMNS)) # tools.generateStrKeyParams(obj.COLUMNS)
        self.__cursor.execute(f'UPDATE {obj.TABLE} SET {str_keyParam} WHERE (id={obj.id})', tuple(obj.getValues().values()))
        self.__conn.commit()

    def deleteObject(self, instance_of_obj):
        obj = instance_of_obj
        self.__checkSubclass(type(obj))

        self.__cursor.execute(f'DELETE FROM {obj.TABLE} WHERE (id={self.__param})', (obj.id, ))
        self.__conn.commit()

    def countTable(self, typeof):
        self.__checkSubclass(typeof)
        self.__cursor.execute(f'SELECT COUNT(*) FROM {typeof.TABLE}')
        return self.__cursor.fetchone()[0]

    #region create
    def createUser(self, *args):
        # verificando se já existe um usuário com esse username
        self.__cursor.execute(f'SELECT id FROM user WHERE username={self.__param}', (args[0], ))
        if self.__cursor.fetchone() is not None:
            raise ApiValueFoundError('já existe um usuário com esse username')
        
        return self.__create(args, User)

    def createBank(self, name, description=None):
        self.__checkUserLogged()

        # verificando se já existe uma conta bancária com esse nome
        self.__cursor.execute(f'SELECT id FROM bank WHERE name={self.__param} AND user_id={self.__param}', (name, self.__currentUser.id))
        if self.__cursor.fetchone() is not None:
            raise ApiValueFoundError('já existe uma conta bancária com esse nome')
        
        args = (name, description, self.__currentUser.id)
        return self.__create(args, Bank)
        
    def createCard(self, num, dia_fechamento, dia_vencimento, limite, bank_id):
        self.__checkUserLogged()

        # verificando se já existe um cartão com esse número para essa conta bancária
        self.__cursor.execute(f'SELECT id FROM card WHERE num={self.__param} AND bank_id={self.__param}', (num, bank_id))
        if self.__cursor.fetchone() is not None:
            raise ApiValueFoundError('já existe um cartão com esse número para essa conta bancária')

        args = (num, dia_fechamento, dia_vencimento, limite, bank_id)
        return self.__create(args, Card)

    def createRegistry(self, type, title, value, datetime, description=None, bank_id=None, card_id=None):
        self.__checkUserLogged()

        args = (type, title, value, datetime, description, self.__currentUser.id, bank_id, card_id)
        return self.__create(args, Registry)
    
    #endregion

    #region get
    def getCurrentUser(self): return self.__currentUser
    # def getAllObjects(self, typeof): return self.__getObject(None, typeof, False)
    def getObject(self, id, typeof): return self.__getObject(typeof, params=(id, ), where_str=f'id={self.__param}')
    def getUser(self, id): return self.__getObject(User, params=(id, ), where_str=f'id={self.__param}')
    def getBank(self, id): return self.__getObject(Bank, params=(id, ), where_str=f'id={self.__param}')
    def getCard(self, id): return self.__getObject(Card, params=(id, ), where_str=f'id={self.__param}')
    def getRegistry(self, id): return self.__getObject(Registry, params=(id, ), where_str=f'id={self.__param}')

    def getCardsByBankId(self, bank_id): return self.__getObject(Card, False, (bank_id, ), f'bank_id={self.__param}')
    
    def getAllBanks(self):
        user_id = self.__currentUser.id if self.__currentUser is not None else None
        return self.__getObject(Bank, False, (user_id, ), f'user_id={self.__param}')
    
    def getNavigationTableInfo(self, typeof, interval=0, limit=DB_ROWS_LIMIT):
        self.__checkConnection()
        self.__checkSubclass(typeof)

        self.__cursor.execute(f'SELECT COUNT(*) FROM {typeof.TABLE}')
        length = self.__cursor.fetchone()[0]
        num_intervals = (length // limit) + (length % limit != 0)

        return NavigationTableInfo(interval, num_intervals, length, limit)

    def getValuesByIndexInterval(self, typeof, *, index_interval=None, info=None):
        if info is None:
            info = self.getNavigationTableInfo(typeof)
            
        elif index_interval is not None:
            info.interval = index_interval

        str_cols, _ = tools.generateStrColumns(typeof.COLUMNS)
        start = info.interval * info.limit

        self.__cursor.execute(f'SELECT {str_cols} FROM `{typeof.TABLE}` LIMIT {start}, {info.limit}')
        return info, [typeof(*r) for r in self.__cursor.fetchall()]

    #endregion

    #endregion
    # -----------------------------------------------
    #region Métodos Privados
    def __checkSubclass(self, typeof):
        if not issubclass(typeof, AbstractTable):
            raise TypeError('o objeto deve ser uma subclasse de AbstractTable')
        
    def __checkConnection(self):
        if not self.isConnected():
            raise ApiConnectionError()
        
    def __checkUserLogged(self):
        if not self.isLogged():
            raise ApiUserNotAuthenticatedError()
        
    def __getObject(self, typeof, unpackWhenOne=True, params=(), where_str=None):
        if typeof not in (User, ):
            self.__checkUserLogged()

        self.__checkSubclass(typeof)

        str_cols, _ = tools.generateStrColumns(typeof.COLUMNS)
        cmd = f'SELECT {str_cols} FROM `{typeof.TABLE}`'

        if where_str:
            cmd += ' WHERE ' + where_str
        
        # if id is None: # retornando todos os resultados
        #     self.__cursor.execute(f'SELECT {str_cols} FROM `{typeof.TABLE}`')
        
        # else:
        #     self.__cursor.execute(f'SELECT {str_cols} FROM `{typeof.TABLE}` WHERE id={self.__param}', (id, ))

        self.__cursor.execute(cmd, params)
        r = self.__cursor.fetchall()
        if not r: # caso retorne None ou empty
            raise ApiValueNotFoundError('dados não encontrados')
        
        data = [typeof(*v) for v in r]
        
        if unpackWhenOne and len(data) == 1:
            return data[0]
        
        return data
    
    def __create(self, args, typeof):
        str_cols, len_cols = tools.generateStrColumns(typeof.COLUMNS, True)
        str_params = ','.join([self.__param for _ in range(len_cols)]) # tools.generateStrParams(len_cols)
        self.__cursor.execute(f'INSERT INTO `{typeof.TABLE}` ({str_cols}) VALUES ({str_params})', args)
        self.__conn.commit()

        return self.__getObject(typeof, params=(self.__cursor.lastrowid, ), where_str=f'id={self.__param}')
    
    #endregion
    # -----------------------------------------------
    