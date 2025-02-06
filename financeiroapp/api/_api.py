from mysql.connector import connect
from mysql.connector.errors import ProgrammingError
from .structs import *
from .consts import *
from .errors import *
from . import tools

class FinanceiroAPI:
    def __init__(self):
        self.__conn = None
        self.__cursor = None
        self.__currentUser = None

    # -----------------------------------------------
    #region Métodos Públicos
    def isLogged(self):
        return self.__currentUser is not None

    def isConnected(self):
        return self.__conn.is_connected() if self.__conn is not None else False
    
    def login(self, username, password):
        self.__checkConnection()
        
        self.__cursor.execute('SELECT id FROM user WHERE username=%s AND password=%s', (username, password))
        r = self.__cursor.fetchone()

        if r is None:
            self.__currentUser = None
            return False
        
        self.__currentUser = self.getUser(r[0])
        return True
    
    def connect(self, **db_params):
        try:
            self.__conn = connect(**db_params)

        except ProgrammingError:
            self.__conn = None
            self.__cursor = None
            return False

        self.__cursor = self.__conn.cursor()
        return True

    def checkCredentials(self, username, password):
        self.__checkConnection()
        
        self.__cursor.execute('SELECT id FROM user WHERE username=%s AND password=%s', (username, password))
        return self.__cursor.fetchone() is not None

    def updateObject(self, instance_of_obj):
        obj = instance_of_obj
        self.__checkSubclass(type(obj))
        
        str_keyParam = tools.generateStrKeyParams(obj.COLUMNS)
        self.__cursor.execute(f'UPDATE {obj.TABLE} SET {str_keyParam} WHERE (id={obj.id})', tuple(obj.getValues().values()))
        self.__conn.commit()

    def deleteObject(self, instance_of_obj):
        obj = instance_of_obj
        self.__checkSubclass(type(obj))

        self.__cursor.execute(f'DELETE FROM {obj.TABLE} WHERE (id=%s)', (obj.id, ))
        self.__conn.commit()

    def countTable(self, typeof):
        self.__checkSubclass(typeof)
        self.__cursor.execute(f'SELECT COUNT(*) FROM {typeof.TABLE}')
        return self.__cursor.fetchone()[0]        

    #region create
    def createUser(self, *args):
        # verificando se já existe um usuário com esse username
        self.__cursor.execute(f'SELECT id FROM user WHERE username=%s', (args[0], ))
        if self.__cursor.fetchone() is not None:
            raise ApiValueFoundError('já existe um usuário com esse username')
        
        return self.__create(args, User, False)

    def createBank(self, name, description=None):
        # verificando se já existe uma conta bancária com esse nome
        self.__cursor.execute(f'SELECT id FROM bank WHERE name=%s', (name, ))
        if self.__cursor.fetchone() is not None:
            raise ApiValueFoundError('já existe uma conta bancária com esse nome')
        
        args = (name, description, self.__currentUser.id)
        return self.__create(args, Bank)
        
    def createCard(self, num, dia_fechamento, dia_vencimento, limite, bank_id):
        # verificando se já existe um cartão com esse número para essa conta bancária
        self.__cursor.execute(f'SELECT id FROM card WHERE num=%s AND bank_id=%s', (num, bank_id))
        if self.__cursor.fetchone() is not None:
            raise ApiValueFoundError('já existe um cartão com esse número para essa conta bancária')

        args = (num, dia_fechamento, dia_vencimento, limite, bank_id)
        return self.__create(args, Card)

    def createRegistry(self, type, title, value, datetime, description=None, bank_id=None, card_id=None):
        args = (type, title, value, datetime, description, self.__currentUser.id, bank_id, card_id)
        return self.__create(args, Registry)
    
    #endregion

    #region get
    def getCurrentUser(self): return self.__currentUser
    def getUser(self, id): return self.__getObject(id, User)
    def getBank(self, id): return self.__getObject(id, Bank)
    def getCard(self, id): return self.__getObject(id, Card)
    def getRegistry(self, id): return self.__getObject(id, Registry)
    
    def getNavigationTableInfo(self, typeof, interval=0, limit=DB_ROWS_LIMIT):
        self.__checkConnection()
        self.__checkSubclass(typeof)

        self.__cursor.execute(f'SELECT COUNT(*) FROM {typeof.TABLE}')
        length = self.__cursor.fetchone()[0]
        num_intervals = (length // limit) + (length % limit != 0)

        return NavigationTableInfo(interval, num_intervals, length, limit)

    def getValuesByIndexInterval(self, typeof, *, index_interval=None, info=None):
        if info is None:
            info = self.getNavigationTableInfo(typeof, index_interval)
            
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
        
    def __getObject(self, id, typeof):
        if typeof not in (User, ):
            self.__checkUserLogged()

        self.__checkSubclass(typeof)

        str_cols, _ = tools.generateStrColumns(typeof.COLUMNS)
        self.__cursor.execute(f'SELECT {str_cols} FROM `{typeof.TABLE}` WHERE id=%s', (id, ))
        r = self.__cursor.fetchone()
        if r is None:
            raise ApiValueNotFoundError(f'dados não encontrados a partir do id {id}')
        
        return typeof(*r)
    
    def __create(self, args, typeof):
        str_cols, len_cols = tools.generateStrColumns(typeof.COLUMNS, True)
        str_params = tools.generateStrParams(len_cols)
        self.__cursor.execute(f'INSERT INTO `{typeof.TABLE}` ({str_cols}) VALUES ({str_params})', args)
        self.__conn.commit()

        return self.__getObject(self.__cursor.lastrowid, typeof)
    
    #endregion
    # -----------------------------------------------
    