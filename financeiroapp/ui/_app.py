from PySide6.QtWidgets import QApplication
from ..controllers._controller import ControllerApp

class Application(QApplication):
    def __init__(self):
        super().__init__()
        self.__controller = ControllerApp(self)

    def exec(self):
        self.__controller.initialize()
        return super().exec()