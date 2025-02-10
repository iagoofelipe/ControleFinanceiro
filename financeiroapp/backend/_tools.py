from PySide6.QtWidgets import QWidget, QMessageBox
import cryptocode
from ._consts import CRYPTO_KEY

def alert(parent:QWidget, msg:str, title='validação de parâmetros', icon=QMessageBox.Icon.Critical):
    return QMessageBox(icon, title,msg, parent=parent).exec()

def encrypt(msg:str):
    return cryptocode.encrypt(msg, CRYPTO_KEY)

def decrypt(msg):
    return cryptocode.decrypt(msg, CRYPTO_KEY)

def getNavigationInfo(length:int, limit:int, index:int) -> tuple[int, int, int, int, int]:
    """
    calcula os valores inicial, final e número de intervalos a partir das informações de length, limit e index.
    Realiza o tratamento de limit e index de acordo com length
    
    retorna start, end, limit, index, num_intervals
    """

    if not (0 < limit < length):
        limit = length

    num_intervals = (length // limit) + (length % limit != 0)

    if length == 0:
        return 0, 0, 0, num_intervals
    
    if index >= num_intervals:
        index = num_intervals - 1

    start = index * limit + 1 # just works if length is bigger than one
    end = (index + 1) * limit if (index + 1 < num_intervals) else length

    return start, end, limit, index, num_intervals