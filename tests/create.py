from financeiroapp.api._api import FinanceiroAPI
from financeiroapp.api.consts import *
import datetime as dt

api = FinanceiroAPI()

if not api.connect(host='localhost', database='financeiro', password='1234', user='test'):
    print('connection error')
    exit()

print('user created', api.createUser('iago', '1234', 'Iago', 'Carvalho'))

bank = api.createBank('Nubank')
print(bank, bank.name)

card = api.createCard('4094', 5, 10, 1500, bank.id)
print(card, card.num)

reg = api.createRegistry(REG_TYPE_IN, 'aulas de piano', 200.30, dt.datetime.now(), 'aluna X')
reg = api.createRegistry(REG_TYPE_OUT, 'livro artes', 40.50, dt.datetime.now(), bank_id=bank.id)
reg = api.createRegistry(REG_TYPE_OUT, 'lanche', 11.50, dt.datetime.now(), card_id=card.id)