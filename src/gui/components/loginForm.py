from PySide6.QtWidgets import QWidget
from PySide6.QtCore import Signal

from .abstractForm import AbstractForm
from ..generated.LoginForm import Ui_LoginForm
from ...backend.consts import PASSWORD_MAX_LEN, USERNAME_MAX_LEN, UI_ID_LOGIN

class LoginForm(AbstractForm):
    continueRequired = Signal()
    ID = UI_ID_LOGIN

    def __init__(self, parent=None):
        super().__init__(parent)
        self.__ui = Ui_LoginForm()

    def setup(self, parent=None):
        self.__wid = wid = QWidget(parent)

        # configurando componentes
        self.__ui.setupUi(wid)
        self.__ui.linePassword.setMaxLength(PASSWORD_MAX_LEN)
        self.__ui.lineUsername.setMaxLength(USERNAME_MAX_LEN)

        # conectando eventos
        self.__ui.pushButton.clicked.connect(self.continueRequired)
        self.__ui.linePassword.returnPressed.connect(self.continueRequired)
        self.__ui.lineUsername.returnPressed.connect(self.continueRequired)

        return wid

    def getEntries(self) -> tuple[str, str, bool]:
        return self.__ui.lineUsername.text(), self.__ui.linePassword.text(), self.__ui.checkBox.isChecked()
    
    def clear(self):
        self.__ui.linePassword.clear()
        self.__ui.lineUsername.clear()