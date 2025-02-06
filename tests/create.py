from financeiroapp.api import FinanceiroAPI
from financeiroapp.api.consts import *
import datetime as dt

api = FinanceiroAPI('sqlite3')
api.connect('database.db')
api.createUser('iago', '1234', 'Iago', 'Carvalho')

bank_nu = api.createBank('Nubank')
bank_mp = api.createBank('Mercado Pago')

card_4094 = api.createCard(4094, 5, 10, 300, bank_nu.id)
card_1303 = api.createCard(1303, 5, 10, 1500, bank_nu.id)
card_7785 = api.createCard(7785, 7, 13, 1500, bank_mp.id)

api.createRegistry(REG_TYPE_IN, 'pagamento', 5000, dt.datetime(2025, 1, 1))
api.createRegistry(REG_TYPE_OUT, 'livro artes', 40.50, dt.datetime(2025, 1, 7), bank_id=bank_mp.id)
api.createRegistry(REG_TYPE_OUT, 'lanche', 9.50, dt.datetime(2025, 1, 7), card_id=card_1303.id)
api.createRegistry(REG_TYPE_OUT, 'lanche', 8.20, dt.datetime(2025, 1, 7), card_id=card_1303.id)
api.createRegistry(REG_TYPE_IN, 'aulas de piano', 200.30, dt.datetime(2025, 1, 9), 'aluna X')
api.createRegistry(REG_TYPE_OUT, 'lanche', 11.50, dt.datetime(2025, 1, 9), card_id=card_1303.id)
api.createRegistry(REG_TYPE_OUT, 'lanche', 11.50, dt.datetime(2025, 1, 9), card_id=card_1303.id)
api.createRegistry(REG_TYPE_IN, 'aulas de piano', 200.30, dt.datetime(2025, 1, 9), 'aluna Y')
api.createRegistry(REG_TYPE_OUT, 'lanche', 11.50, dt.datetime(2025, 1, 9), card_id=card_4094.id)
api.createRegistry(REG_TYPE_OUT, 'lanche', 11.50, dt.datetime(2025, 1, 10), card_id=card_4094.id)
api.createRegistry(REG_TYPE_OUT, 'passagem ônibus', 5.5, dt.datetime(2025, 1, 15), card_id=card_7785.id)
api.createRegistry(REG_TYPE_OUT, 'passagem ônibus', 5.5, dt.datetime(2025, 1, 15), card_id=card_7785.id)