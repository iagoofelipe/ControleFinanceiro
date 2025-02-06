from mysql.connector import connect

params = dict(host='localhost', database='world', password='1234', user='test')
conn = connect(**params)
cursor = conn.cursor()

# length = 10
# limit = 3
# interval = 1 # [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10]]
# values = list(range(1, 11))

cursor.execute('SELECT COUNT(*) FROM country')
length = cursor.fetchone()[0] # 239
limit = 10
interval = 23

intervals = (length // limit) + (length % limit != 0)
start = interval * limit
num = limit

print(f'LIMT {start}, {num}')

cursor.execute(f'SELECT Name FROM country LIMIT {start}, {num}')
print(cursor.fetchall())