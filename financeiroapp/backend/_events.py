from PySide6.QtCore import QObject, Signal

class ViewAppEvents(QObject):
    initializationStarted = Signal()
    initializationFinished = Signal()
    setupPageRequired = Signal(int)
    currentPageChanged = Signal(int)

class ControllerAppEvents(QObject):
    initializationStarted = Signal()
    initializationFinished = Signal()

class ModelAppEvents(QObject):
    initializationStarted = Signal()
    initializationFinished = Signal()

class EventHandlerApp(QObject):
    def __init__(self, parent:QObject):
        super().__init__(parent, objectName='EventHandlerApp')
        self.__model = ModelAppEvents(self)
        self.__view = ViewAppEvents(self)
        self.__controller = ControllerAppEvents(self)

    @property
    def view(self):
        return self.__view
    
    @property
    def model(self):
        return self.__model
    
    @property
    def controller(self):
        return self.__controller