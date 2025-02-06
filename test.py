from mysql.connector import connect
from financeiroapp.api import FinanceiroAPI
from financeiroapp.api.structs import AbstractTable

params = dict(host='localhost', database='world', password='1234', user='test')
# conn = connect(**params)
# cursor = conn.cursor()

# cursor.execute('SELECT COUNT(*) FROM country')
# length = cursor.fetchone()[0] # 239
# limit = 10
# interval = 23

# intervals = (length // limit) + (length % limit != 0)
# start = interval * limit
# num = limit

# print(f'LIMT {start}, {num}')

# cursor.execute(f'SELECT Name FROM country LIMIT {start}, {num}')
# print(cursor.fetchall())

api = FinanceiroAPI()
api.connect(**params)

class Country(AbstractTable):
    COLUMNS = ('Name', 'Continent')
    TABLE = 'country'
    Name:str
    Continent:str

    def __init__(self, *args):
        super().__init__(*args)

info = api.getNavigationTableInfo(Country)
print(info)
print(info.length)
print(info.num_intervals)
print(info.limit)

info.interval = 1
rows = api.getValuesByIndexInterval(Country, info=info)
print(rows)