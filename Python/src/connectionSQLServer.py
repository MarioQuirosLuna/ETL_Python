import pyodbc

try:
    connection = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=localhost;DATABASE=database;UID=user;PWD=pass')
    #connection = pyodbc.connect('DRIVER={SQL Server};SERVER=LOCALHOST;DATABASE=Test_ETL;Trusted_Connection=yes')
    print('Conexion Exitosa')
    cursor = connection.cursor()
    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()
    print(row)
    cursor.execute('SELECT * FROM [CLI_COMMON].[tb_CLIENTS]')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except Exception as ex:
    print(ex)
finally:
    connection.close()
    print("Conexion finalizada")
