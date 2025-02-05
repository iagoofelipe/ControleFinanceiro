from PySide6.QtCore import QObject
from PySide6.QtWidgets import QWidget

from ...models._model import ModelApp 
from ...ui.auto.ui_LoginPage import Ui_LoginPage
from ...backend._consts import *
from ...backend import _tools as tools

class LoginPage(QObject):
    PAGE_ID = PAGE_ID_LOGIN

    def __init__(self, parent:QObject, model:ModelApp):
        super().__init__(parent, objectName='ViewApp')
        self.__model = model
        self.__isCurrentPage = False
        self.__ui = Ui_LoginPage()

        # conectando eventos
        model.events.loginRequired.connect(self.on_model_loginRequired)
        model.events.loginFinished.connect(self.on_model_loginFinished)
        model.eventHandler.view.currentPageChanged.connect(self.on_view_currentPageChanged)

    def setup(self, parent:QWidget) -> QWidget:
        self.__wid = QWidget(parent)
        self.__ui.setupUi(self.__wid)

        # conectando eventos
        self.__ui.lineUsername.returnPressed.connect(self.__ui.btnLogin.click)
        self.__ui.linePassword.returnPressed.connect(self.__ui.btnLogin.click)
        self.__ui.btnLogin.clicked.connect(self.on_btnLogin_clicked)

        return self.__wid

    # -----------------------------------------------------------------
    # Slots
    def on_view_currentPageChanged(self, pageId:int):
        self.__isCurrentPage = self.PAGE_ID == pageId

    def on_btnLogin_clicked(self):
        self.__model.logger.debug('LoginPage::on_btnLogin_clicked')
        username = self.__ui.lineUsername.text()
        password = self.__ui.linePassword.text()
        remember = self.__ui.cbRemember.isChecked()

        if not username or not password:
            tools.alert(self.__wid, 'preencha todos os campos!')
            return
        
        self.__model.login(username, password, remember)

    def on_model_loginRequired(self):
        if not self.__isCurrentPage:
            return
        
        self.__model.logger.debug('LoginPage::on_model_loginRequired')
        self.__ui.btnLogin.setDisabled(True)
    
    def on_model_loginFinished(self, success:bool):
        if not self.__isCurrentPage:
            return
        
        self.__model.logger.debug(f'LoginPage::on_model_loginFinished <isCurrentPage={self.__isCurrentPage} success={success}>')

        if not success:
            tools.alert(self.__wid, 'usuário ou senha inválidos!')
            self.__ui.btnLogin.setDisabled(False)
    