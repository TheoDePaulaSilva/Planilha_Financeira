import pymysql

conexaobd = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='Planilha_Financeira'
)

cursor = conexaobd.cursor()
sql = 'select * from usuario'
cursor.execute(sql)
resultados = cursor.fetchall()
print(resultados)