import pymysql
import bcrypt
import datetime

conexaobd = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='Planilha_Financeira'
)

def cadastro():
    cursor = conexaobd.cursor()
    nome = input('Insira seu nome completo: ').strip()
    while  not all(c.isalpha() or c.isspace() for c in nome):
        nome = input('Nome inválido!! Insira novamente: ').strip()
    email = input('Insira seu email: ')
    cursor.execute('select email from usuario')
    email_exist = cursor.fetchall()
    if len(email_exist) != 0:
        for i in email_exist:
            while i == email:
                email = input('O email ja existe!!\nTente novamente: ')
    senha = input('Insira uma senha: ')
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'),bcrypt.gensalt())
    data_criacao = datetime.date.today()
    cod_id = 'select id from usuario order by id desc limit 1'
    cursor.execute(cod_id)
    if cursor.fetchone() == None:
        id = 1
    else:
        id = int(cursor.fetchone())+1
    cod_add = 'insert into usuario values (%s,%s,%s,%s,%s)'
    val = (id,nome,email,senha_hash,data_criacao)
    cursor.execute(cod_add,val)
    conexaobd.commit()

cadastro()