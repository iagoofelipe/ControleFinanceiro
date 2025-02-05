import datetime
from typing import Any

__all__ = ['REG_TYPE', 'AbstractTable', 'User', 'Bank', 'Card', 'Registry']

REG_TYPE = int

class AbstractTable:
    COLUMNS:tuple[str]
    TABLE:str

    def getValues(self) -> dict[str, Any]: ...

class User(AbstractTable):
    id:int
    username:str
    password:str
    first_name:str
    last_name:str

class Bank(AbstractTable):
    id:int
    name:str
    description:str
    user_id:int

class Card(AbstractTable):
    id:int
    num:int
    nome:str
    d_vencimento:int
    d_fechamento:int
    limite:int
    bank_id:int

class Registry(AbstractTable):
    id:int
    type:REG_TYPE
    title:str
    value:float
    datetime:datetime.datetime
    description:str | None
    user_id:int | None
    bank_id:int | None
    card_id:int | None
