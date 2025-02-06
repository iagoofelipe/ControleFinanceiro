from .consts import *

class AbstractObject:
    ATTRIBUTES = None

    def __init__(self, *args):
        for i, a in enumerate(self.ATTRIBUTES):
            self.__setattr__(a, args[i])

    def __repr__(self):
        return self.__str__()

class AbstractTable(AbstractObject):
    COLUMNS = None
    TABLE = 'AbstractTable'

    def __init__(self, *args):
        self.ATTRIBUTES = self.COLUMNS
        super().__init__(*args)

    def __str__(self):
        return f'<{self.__class__.__name__} id={self.id}>'
    
    def getValues(self):
        return {col: self.__getattribute__(col) for col in self.COLUMNS}

class NavigationTableInfo(AbstractObject):
    ATTRIBUTES = ('num_intervals', 'length', 'limit')

    def __init__(self, *args):
        super().__init__(*args)

class User(AbstractTable):
    COLUMNS = DB_COLS_TABLE_USER
    TABLE = 'user'

    def __init__(self, *args):
        super().__init__(*args)


class Bank(AbstractTable): 
    COLUMNS = DB_COLS_TABLE_BANK
    TABLE = 'bank'

    def __init__(self, *args):
        super().__init__(*args)


class Card(AbstractTable):
    COLUMNS = DB_COLS_TABLE_CARD
    TABLE = 'card'

    def __init__(self, *args):
        super().__init__(*args)


class Registry(AbstractTable):
    COLUMNS = DB_COLS_TABLE_REGISTRY
    TABLE = 'registry'

    def __init__(self, *args):
        super().__init__(*args)
