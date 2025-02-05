from PySide6.QtCore import QObject, Signal, Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel

from ...models._model import ModelApp 
from ...backend._consts import *

class LoadingPage(QObject):
    messageChanged = Signal(str)

    PAGE_ID = PAGE_ID_LOADING

    def __init__(self, parent:QObject, model:ModelApp):
        super().__init__(parent, objectName='ViewApp')
        self.__model = model
        self.__isCurrentPage = False
        self.__label = None

        # conectando eventos
        model.eventHandler.view.currentPageChanged.connect(self.on_view_currentPageChanged)

    def setup(self, parent:QWidget) -> QWidget:
        wid = QWidget(parent)
        layout = QVBoxLayout(wid)
        self.__label = QLabel('inicializando componentes...', wid)
        self.__label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        layout.addWidget(self.__label)

        return wid

    def setMessage(self, msg:str):
        if not self.__isCurrentPage:
            raise ValueError('[LoadingPage::setMessage] LoadingPage is not the current page')
        
        self.__label.setText(msg)
        self.messageChanged.emit(msg)

    # -----------------------------------------------------------------
    # Slots
    def on_view_currentPageChanged(self, pageId:int):
        self.__isCurrentPage = self.PAGE_ID == pageId
