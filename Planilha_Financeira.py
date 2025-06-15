import pymysql
import bcrypt
import datetime
from tkinter import *

def cadastro():
    conexaobd = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='Noceutempao-123',
    database='Planilha_Financeira'
    )
    cursor = conexaobd.cursor()
    nome = input('Insira seu nome completo: ').strip()
    while  not all(c.isalpha() or c.isspace() for c in nome):
        nome = input('Nome inválido!! Insira novamente: ').strip()
    while True:
        email = input('Insira seu email: ').strip()
        cursor.execute('SELECT email FROM usuario WHERE email = %s', (email))
        if cursor.fetchone() is None:
            break
        else:
            print('O email já existe! Tente outro.')
    senha = input('Insira uma senha: ')
    while senha != input('Repita sua senha: '):
        print('A senhas são diferentes!!')
    senha_hash = bcrypt.hashpw(senha.encode('utf-8'),bcrypt.gensalt())
    data_criacao = datetime.date.today()
    cod_id = 'select id from usuario order by id desc limit 1'
    cursor.execute(cod_id)
    result = cursor.fetchone()
    if result is None:
        id = 1
    else:
        id = int(result[0])+1
    cod_add = 'insert into usuario values (%s,%s,%s,%s,%s)'
    val = (id,nome,email,senha_hash,data_criacao)
    cursor.execute(cod_add,val)
    conexaobd.commit()
    conexaobd.close()

cadastro()

janela = Tk()
janela.title('Planilha Financeira')

janela.mainloop()