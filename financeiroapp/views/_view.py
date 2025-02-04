from PySide6.QtCore import QObject, Qt
from PySide6.QtWidgets import QMainWindow, QWidget
from PySide6.QtGui import QGuiApplication

from ..models._model import ModelApp
from ..ui.pages._loading import LoadingPage
from ..ui.pages._reg import RegistryPage
from ..ui.auto.ui_MainWindow import Ui_MainWindow
from ..backend._consts import *

class ViewApp(QObject):
    def __init__(self, parent:QObject, model:ModelApp):
        super().__init__(parent, objectName='ViewApp')
        self.__model = model
        self.__events = model.eventHandler.view
        self.__currentPage = None
        self.__currentNavBtn = None
        self.__loadingPage = LoadingPage(self, model)
        self.__regPage = RegistryPage(self, model)
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
        self.events.initializationStarted.emit()
        
        QGuiApplication.styleHints().setColorScheme(Qt.ColorScheme.Light)
        self.setupPageById(PAGE_ID_LOADING)
        self.__window.resize(1000, 600)
        self.__window.setWindowTitle('Controle Financeiro')

        self.__window.show()
        self.events.initializationFinished.emit()

    def setupPageById(self, pageId:int):

        # para páginas que utilizam MainWindow
        if pageId in MAINWINDOW_PAGES and self.__currentPage not in MAINWINDOW_PAGES:
            self.__setupMainWindow()

        # definindo conteúdo da página
        if pageId == PAGE_ID_LOADING:
            self.__window.setCentralWidget(self.__loadingPage.setup(None))
            self.__currentNavBtn = None  # não utiliza MainWindow

        elif pageId in MAINWINDOW_PAGES:
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
        if pageId == PAGE_ID_HOME:
            wid_new = QWidget(self.__wid)
            navBtn = self.__ui.btnHome

        elif pageId == PAGE_ID_REG:
            wid_new = self.__regPage.setup(self.__wid)
            navBtn = self.__ui.btnReg

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
