from multiprocessing import connection
import psycopg2

try:
    connection = psycopg2.connect(
        host='localhost',
        user='user',
        password='12345',
        database='database'
    )

    print('Conexion exitosa')
    cursor = connection.cursor()
    cursor.execute("SELECT version()")
    row = cursor.fetchone()
    print(row)
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("Conexion finalizada")
