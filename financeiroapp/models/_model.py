from PySide6.QtCore import QObject, Signal
from threading import Thread
from time import sleep

from ..backend._events import EventHandlerApp

class ModelApp(QObject):
    def __init__(self, parent:QObject):
        super().__init__(parent, objectName='ModelApp')
        self.__eventHandler = EventHandlerApp(self)
        self.__events = self.__eventHandler.model

    # -----------------------------------------------------------------
    # Propriedades
    @property
    def events(self):
        return self.__events
    
    # Propriedades
    @property
    def eventHandler(self):
        return self.__eventHandler

    # -----------------------------------------------------------------
    # Métodos Públicos
    def initialize(self):
        self.events.initializationStarted.emit()

        def func():
            # sleep(2)
            self.events.initializationFinished.emit()

        Thread(target=func).start()
        
    # -----------------------------------------------------------------
    # Métodos Privados