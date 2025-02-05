from PySide6.QtCore import QObject, Signal, Qt
from PySide6.QtWidgets import QWidget

from ...ui.auto.ui_RegistryPage import Ui_RegistryPage
from ...backend._consts import *
from ...models._model import ModelApp 
from ...ui.components._table import Table

class RegistryPage(QObject):
    def __init__(self, parent:QObject, model:ModelApp):
        super().__init__(parent, objectName='ViewApp')
        self.__model = model
        self.__ui = Ui_RegistryPage()
        self.__wid = None
        self.__tableHistorico = None

    def setup(self, parent:QWidget) -> QWidget:
        self.__wid = QWidget(parent)
        self.__ui.setupUi(self.__wid)

        # Historico
        self.__tableHistorico = Table(self.__ui.widHistorico, title='Histórico de Registros', flags={TABLE_HEADER_DELETE})
        wid_new = self.__tableHistorico
        wid_old = self.__ui.widHistoricoTable
        self.__ui.widHistoricoTable = wid_new

        self.__ui.historicoLayout.replaceWidget(wid_old, wid_new)
        wid_old.deleteLater()

        # Agendados
        self.__tableAgendados = Table(self.__ui.widAgendados, title='Registros Agendados', flags={TABLE_HEADER_DELETE})
        wid_new = self.__tableAgendados
        wid_old = self.__ui.widAgendadosTable
        self.__ui.widAgendadosTable = wid_new

        self.__ui.agendadosLayout.replaceWidget(wid_old, wid_new)
        wid_old.deleteLater()

        

        self.reset()

        return self.__wid
    
    def reset(self):
        pass