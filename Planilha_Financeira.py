import pymysql
import bcrypt
import datetime
from tkinter import *
from PIL import Image, ImageTk

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
        senha = input('Insira sua senha: ')
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

def login():
    conexaobd = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='Noceutempao-123',
    database='Planilha_Financeira'
    )
    cursor = conexaobd.cursor()
    email = input('Insira seu emai: ').strip()
    cursor.execute('SELECT email FROM usuario WHERE email = %s', (email))
    if cursor.fetchone() is None:
        print('O cadastro não existe!!')
        res = int(input('Deseja fazer cadastro? 1 para sim e 0 para não: '))
        if res:
            cadastro()
    else:
        senha = input('Insira sua senha: ')
        cursor.execute('SELECT senha_hash FROM usuario WHERE email = %s',(email))
        senha_hash = cursor.fetchone()[0].encode('utf-8')
        if bcrypt.checkpw(senha.encode('utf-8'), senha_hash):
            print("Senha correta!")
        else:
            print("Senha incorreta.")
    conexaobd.close()


inicio = Tk()
inicio.title('Planilha Financeira')
imagem_pil = Image.open("icone.png")
imagem = imagem_pil.resize((250, 250))
icone = ImageTk.PhotoImage(imagem)
inicio.iconphoto(False, icone)
titulo = Label(inicio, text = 'Planilha Financeira', font = ('Arial', 40, 'bold'), padx=80,pady=80)
titulo.grid(row = 1, column=1)
label = Label(inicio, image=icone,padx=80,pady=80)
label.grid(row=0, column = 1)

inicio.mainloop()