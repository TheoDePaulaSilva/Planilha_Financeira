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
    tela_cad.configure(bg = 'gray15')
    tela_cad.columnconfigure(0, weight=1)
    espaco = Label(tela_cad, height=1, bg='gray15')
    espaco.grid(row = 0, column=0)
    tela_cad.geometry("500x700")
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
        email = input('Insira seu email: ').strip().lower()
        cursor.execute('SELECT email FROM usuario WHERE email = %s', (email,))
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
    tela_log.columnconfigure(0, weight=1)
    espaco = Label(tela_log, height=1, bg='gray15')
    espaco.grid(row = 0, column=0)
    tela_log.geometry("500x650")

    def verificarLogin():
        email = cx_email.get().strip().lower()
        senha = cx_senha.get()

        if not email and not senha:
            txt_email.configure(fg = 'red2')
            txt_senha.configure(fg = 'red2')
        elif not email:
            txt_email.configure(fg = 'red2')
            txt_senha.configure(fg = 'white')
        elif not senha:
            txt_senha.configure(fg = 'red2')
            txt_email.configure(fg = 'white')
        else:
            txt_email.configure(fg = 'white')
            txt_senha.configure(fg = 'white')

            conexaobd = pymysql.connect(
            host='127.0.0.1',
            user='root',
            password='Noceutempao-123',
            database='Planilha_Financeira'
            )
            cursor = conexaobd.cursor()
            cursor.execute('SELECT email FROM usuario WHERE email = %s', (email,))
            if cursor.fetchone() is None:
                print('O cadastro não existe!!')
                res = int(input('Deseja fazer cadastro? 1 para sim e 0 para não: '))
                if res:
                    cadastro()
            else:
                cursor.execute('SELECT senha_hash FROM usuario WHERE email = %s',(email,))
                senha_hash = cursor.fetchone()[0].encode('utf-8')
                if bcrypt.checkpw(senha.encode('utf-8'), senha_hash):
                    print("Senha correta!")
                    cursor.execute('SELECT nome FROM usuario WHERE email = %s',(email,))
                    atual_user = cursor.fetchone()[0]
                    print(f'O usuario atual é: {atual_user}')
                else:
                    print("Senha incorreta!!")
            conexaobd.close()

    imagem_pil = Image.open("icone.png")
    icone_log = ImageTk.PhotoImage(imagem_pil.resize((150, 150)))
    imagem_log = Label(tela_log, image = icone_log)
    imagem_log.image = icone_log
    imagem_log.grid(row = 1, column = 0, padx = 10, pady = 30)

    titulo_log = Label(tela_log, text = 'Entrar', bg = 'gray15', fg = 'white', font = ('Arial', 30, 'bold'), padx = 10, pady = 10)
    titulo_log.grid(row = 2, column = 0)

    txt_email = Label(tela_log, text = '*Email:', bg = 'gray15', fg = 'white', padx = 10, pady = 10, font = ('Arial', 20, 'bold'))
    txt_email.grid(row = 3, column = 0)
    cx_email = Entry(tela_log, font = ('Arial', 15))
    cx_email.grid(row = 4, column = 0, pady = 10, padx = 10)

    txt_senha = Label(tela_log, text = '*Senha:', bg = 'gray15', fg = 'white', padx = 10, pady = 10, font = ('Arial', 20, 'bold'))
    txt_senha.grid(row = 5, column = 0)
    cx_senha = Entry(tela_log, font = ('Arial', 15), show = '*')
    cx_senha.grid(row = 6, column = 0, pady = 10, padx = 10)

    botao_log = Button(tela_log, text = 'Entrar', bg = 'gray80', fg = "#212121", font = ('Arial', 20, 'bold'), command = verificarLogin)
    botao_log.grid(row = 8, column = 0, padx = 10, pady = 10)

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