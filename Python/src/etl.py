from decouple import config
import psycopg2
import pyodbc

try:
    connectionPostgreSQL = psycopg2.connect(
        host=config('POSGRESQL_HOST'),
        user=config('POSGRESQL_USER'),
        password=config('POSGRESQL_PASS'),
        database=config('POSGRESQL_DATABASE')
    )
    print('Connection successfully to PosgreSQL')
    with connectionPostgreSQL.cursor() as cursorPosgreSQL:
        cursorPosgreSQL.execute("SELECT * FROM users")
        temp = cursorPosgreSQL.fetchall()

        connectionSQLServer = pyodbc.connect(
            'DRIVER={SQL Server};SERVER='+config('SQLSERVER_HOST')+';DATABASE='+config(
                'SQLSERVER_DATABASE')+';UID='+config('SQLSERVER_USER')+';PWD='+config('SQLSERVER_PASS')
        )

        print('Connection successfully to SQLServer')
        with connectionSQLServer.cursor() as cursorSQLServer:
            for aux in temp:
                query = 'INSERT INTO dbo.nombres VALUES(?,?);'
                cursorSQLServer.execute(query, (aux[1], aux[2]))
            print("Inserts successfull")

except Exception as ex:
    print("Error with connection ", ex)
finally:
    print("Connection close")
    connectionPostgreSQL.close()
    connectionSQLServer.close()
