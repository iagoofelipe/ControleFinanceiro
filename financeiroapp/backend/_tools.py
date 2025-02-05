from PySide6.QtWidgets import QWidget, QMessageBox
import cryptocode
from ._consts import CRYPTO_KEY

def alert(parent:QWidget, msg:str, title='validação de parâmetros', icon=QMessageBox.Icon.Critical):
    return QMessageBox(icon, title,msg, parent=parent).exec()

def encrypt(msg:str):
    return cryptocode.encrypt(msg, CRYPTO_KEY)

def decrypt(msg):
    return cryptocode.decrypt(msg, CRYPTO_KEY)