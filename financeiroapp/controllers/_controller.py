from PySide6.QtCore import QObject

from ..models._model import ModelApp
from ..views._view import ViewApp
from ..backend._consts import *

class ControllerApp(QObject):
    def __init__(self, parent:QObject):
        super().__init__(parent, objectName='ControllerApp')
        self.__model = ModelApp(self)
        self.__view = ViewApp(self, self.__model)
        self.__events = self.__model.eventHandler.controller

        # conectando eventos
        self.model.events.initializationFinished.connect(self.on_model_initializationFinished)

    # -----------------------------------------------------------------
    # Propriedades
    @property
    def view(self):
        return self.__view
    
    @property
    def model(self):
        return self.__model
    
    @property
    def events(self):
        return self.__events
    
    # -----------------------------------------------------------------
    # Métodos Públicos
    def initialize(self):
        self.view.initialize()
        self.model.initialize()
        
    # -----------------------------------------------------------------
    # slots
    def on_model_initializationFinished(self):
        # pageLoading = self.view.getPageById(PAGE_ID_LOADING)
        # pageLoading.setMessage('inicialização finalizada')
        self.view.setupPageById(PAGE_ID_REG)