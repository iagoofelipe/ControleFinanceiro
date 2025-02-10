from PySide6.QtCore import QObject, Qt
from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtGui import QGuiApplication

from ..models._model import ModelApp
from .pages._loading import LoadingPage
from .pages._reg import RegistryPage
from .pages._login import LoginPage
from ..ui.auto.ui_MainWindow import Ui_MainWindow
from ..backend._consts import *

class ViewApp(QObject):
    def __init__(self, parent:QObject, model:ModelApp):
        super().__init__(parent, objectName='ViewApp')
        QGuiApplication.styleHints().setColorScheme(Qt.ColorScheme.Light)
        
        self.__model = model
        self.__events = model.eventHandler.view
        self.__currentPage = None
        self.__currentNavBtn = None
        self.__loadingPage = LoadingPage(self, model)
        self.__regPage = RegistryPage(self, model)
        self.__loginPage = LoginPage(self, model)
        self.__window = QMainWindow()
        self.__ui = Ui_MainWindow()
        self.__wid = None

    # -----------------------------------------------------------------
    # Propriedades
    @property
    def model(self):
        return self.__model
    
    @property
    def events(self):
        return self.__events
    
    # -----------------------------------------------------------------
    # Métodos Públicos
    def initialize(self):
        self.__model.logger.debug(f'ViewApp::initialize')
        self.events.initializationStarted.emit()
        
        self.setupPageById(PAGE_ID_LOADING)
        self.__window.resize(1000, 600)
        self.__window.setWindowTitle(WINDOW_TITLE)

        self.__window.show()
        self.events.initializationFinished.emit()

    def setupPageById(self, pageId:int):
        self.__model.logger.debug(f'ViewApp::setupPageById <pageId={pageId}>')

        # para páginas que utilizam MainWindow
        if self.__currentPage not in WINDOW_PAGES:
            self.__currentNavBtn = None

            if pageId in WINDOW_PAGES:
                self.__setupMainWindow()

        # definindo conteúdo da página
        if pageId == PAGE_ID_LOADING:
            self.__window.setCentralWidget(self.__loadingPage.setup(None))
            self.__window.setWindowTitle(WINDOW_TITLE)

        elif pageId == PAGE_ID_LOGIN:
            self.__window.setCentralWidget(self.__loginPage.setup(None))
            self.__window.setWindowTitle(WINDOW_TITLE + ' | Login')

        elif pageId in WINDOW_PAGES:
            self.__changeMainWindowContent(pageId)

        else:
            raise ValueError(f'page id {pageId} undefined')
        
        self.__currentPage = pageId
        self.events.currentPageChanged.emit(pageId)

    def getPageById(self, pageId:int) -> LoadingPage | None:
        if pageId == PAGE_ID_LOADING:
           return self.__loadingPage
        else:
            raise ValueError(f'page id {pageId} undefined')
        
    def checkCurrentPageById(self, pageId:int) -> bool:
        return self.__currentPage == pageId

    # -----------------------------------------------------------------
    # Métodos Privados
    def __setupMainWindow(self):
        self.__wid = QWidget()
        self.__ui.setupUi(self.__wid)
        self.__window.setCentralWidget(self.__wid)

        # conectando eventos
        self.__ui.btnHome.clicked.connect(lambda: self.setupPageById(PAGE_ID_HOME))
        self.__ui.btnReg.clicked.connect(lambda: self.setupPageById(PAGE_ID_REG))

    def __changeMainWindowContent(self, pageId:int):
        windowTitle = WINDOW_TITLE

        if pageId == PAGE_ID_HOME:
            wid_new = QWidget(self.__wid)
            navBtn = self.__ui.btnHome
            windowTitle += ' | Home'

        elif pageId == PAGE_ID_REG:
            wid_new = self.__regPage.setup(self.__wid)
            navBtn = self.__ui.btnReg
            windowTitle += ' | Registros'

        else:
            raise ValueError(f'page id {pageId} is not a valid MainWindowPage')

        # alterando botão de sidebar para o conteúdo atual
        if self.__currentNavBtn is not None:
            self.__currentNavBtn.setEnabled(True)

        self.__currentNavBtn = navBtn
        wid_old = self.__ui.widContent
        self.__ui.widContent = wid_new
        
        self.__ui.mainLayout.replaceWidget(wid_old, wid_new)
        wid_old.deleteLater()
        navBtn.setEnabled(False)
        self.__window.setWindowTitle(windowTitle)
