import pymysql
import bcrypt
import datetime
from tkinter import *
from PIL import Image, ImageTk

def cadastro():
    inicio.withdraw()
    tela_cad = Toplevel(inicio)
    tela_cad.title('Conectar')
    tela_cad.iconphoto(False, icone)
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
    cod_add = 'insert into usuario (nome, email, senha_hash, data_criacao) values (%s,%s,%s,%s)'
    val = (nome,email,senha_hash,data_criacao)
    cursor.execute(cod_add,val)
    conexaobd.commit()
    conexaobd.close()

def login():
    inicio.withdraw()
    tela_log = Toplevel(inicio)
    tela_log.title('Entrar')
    tela_log.iconphoto(False, icone)
    tela_log.configure(bg = 'gray15')

    conexaobd = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='Noceutempao-123',
    database='Planilha_Financeira'
    )
    cursor = conexaobd.cursor()

    cx_email = Entry(tela_log)
    cx_email.grid(row = 15, column = 0)
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
inicio.configure(bg = 'gray15')

inicio.columnconfigure(0, weight=1)
for i in range(6):
    inicio.rowconfigure(i, weight=1)

imagem_pil = Image.open("icone.png")
imagem = imagem_pil.resize((250, 250))
icone = ImageTk.PhotoImage(imagem)
inicio.iconphoto(False, icone)

espaco = Label(inicio, height=2, bg='gray15')
espaco.grid(row = 0, column=0)

img = Label(inicio, image = icone, padx = 80, pady = 80)
img.grid(row=1, column = 0)

titulo = Label(inicio, text = 'Planilha Financeira', font = ('Arial', 40, 'bold'), padx=80,pady=80, bg = 'gray15', fg = 'white')
titulo.grid(row = 2, column=0)

but_Cad = Button(inicio, text = 'Cadastrar', command = cadastro, font = ('Arial', 20, 'bold'), bg = 'gold1')
but_Cad.grid(row = 3, column = 0, padx = 10, pady = 10)

but_Log = Button(inicio, text = 'Entrar', command = login, font = ('Arial', 20, 'bold'), bg = 'gray80', fg = '#212121')
but_Log.grid(row = 4, column = 0, padx = 20, pady = 20)


inicio.mainloop()