from financeiroapp.api import FinanceiroAPI
from financeiroapp.api.consts import *
from uuid import uuid4

api = FinanceiroAPI()

if not api.connect(host='localhost', database='financeiro', password='1234', user='test'):
    print('connection error')
    exit()

# caso não haja este usuário
if not api.checkCredentials('iago', '1234'):
    print('user created', api.createUser('iago', '1234', 'Iago', 'Carvalho'))

if not api.login('iago', '1234'):
    print('invalid credentials')
    exit()

print('current user', api.getCurrentUser())

# bank = api.createBank('Nubank')
# print(bank, bank.name)

# card = api.createCard('4094', 5, 10, 1500, bank.id)
# print(card, card.num)

# reg = api.createRegistry(REG_TYPE_IN, 'aulas de piano', 200.30, dt.datetime.now(), 'aluna X')
# reg = api.createRegistry(REG_TYPE_OUT, 'livro artes', 40.50, dt.datetime.now(), bank_id=bank.id)
# reg = api.createRegistry(REG_TYPE_OUT, 'lanche', 11.50, dt.datetime.now(), card_id=card.id)


reg = api.getRegistry(2)
print(reg, f'title: "{reg.title}", value: {reg.value}')
reg.title = 'livro ' + str(uuid4()).upper()
api.updateObject(reg)

reg = api.getRegistry(reg.id)
print(reg, f'title: "{reg.title}", value: {reg.value}')