from financeiroapp import api

obj = api.FinanceiroAPI('sqlite3')
obj.connect('database.db')
obj.login('iago', '1234')
info = obj.getNavigationTableInfo(api.structs.Bank)