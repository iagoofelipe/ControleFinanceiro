from mysql.connector import connect
import time


while True:
    start = time.time()

    con = connect(host='localhost', username='test', password='1234', database='financeiro')
    cursor = con.cursor()

    try:
        cursor.execute('SELECT * FROM usuario WHERE id=1')
        print(cursor.fetchone())
        time.sleep(1)
    
    except KeyboardInterrupt:
        break

    cursor.close()
    con.close()
    print('Duration', time.time() - start)