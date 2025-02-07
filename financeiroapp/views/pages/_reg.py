from PySide6.QtCore import QObject, Signal, Qt, QDate
from PySide6.QtWidgets import QWidget
from typing import Iterable

from ... import api
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
        self.__cards_by_bank = {}

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

        # definindo configurações
        self.__ui.dtEditDatahora.setMaximumDate(QDate(CURRENT_DATE.year, 12, 31))
        self.__ui.comboConta.currentIndexChanged.connect(self.on_comboConta_currentIndexChanged)

        self.reset()

        return self.__wid
    
    def reset(self):
        self.resetCadastros()

    def resetCadastros(self):
        self.__ui.radionBtnSaida.click()
        self.__ui.lineTitulo.clear()
        self.__ui.doubleSpinValor.setValue(1)
        self.__ui.lineDescricao.clear()
        self.__ui.comboConta.clear()
        self.__ui.comboCartao.clear()
        self.__ui.cbRecorrencia.setChecked(False)
        self.__ui.spinRecorrencia.setValue(1)

        # inserindo valores de ComboBox
        self.updateBanks(self.__model.api.getAllBanks())
        # self.updateCards(self.__model.api.getAllObjects(api.structs.Card))

    def updateBanks(self, banks:Iterable[api.structs.Bank]):
        self.__banks = banks
        self.__cards_by_bank.clear()
        self.__ui.comboCartao.clear()
        self.__ui.comboConta.addItems([b.name for b in self.__banks])

    def updateCards(self, cards:Iterable[api.structs.Card]):
        self.__cards = cards
        self.__ui.comboCartao.clear()
        self.__ui.comboCartao.addItems([str(c.num) for c in self.__cards])

    def on_comboConta_currentIndexChanged(self, index:int):
        bank = self.__banks[index]

        if bank in self.__cards_by_bank:
            cards = self.__cards_by_bank[bank]
        else:
            print('getting cards to bank', bank.name)
            cards = self.__model.api.getCardsByBankId(bank.id)
            self.__cards_by_bank[bank] = cards

        self.updateCards(cards)

        
        