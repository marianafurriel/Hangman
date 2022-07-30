from tkinter import *
from jogar import jogar
from add_palavra import add_palavra

def escrever():
    texto = "oi\noi\noi\noi"
    texto_orientacao2 = Label(janela, text=texto)
    texto_orientacao2.grid(column=0,row=2)

janela = Tk()
janela.title("Hangman")
texto_orientacao = Label(janela, text="Bem vindo! O que deseja fazer?")
texto_orientacao.grid(column=0,row=0)

botao_jogar = Button(janela,text="Jogar",command=jogar)
botao_jogar.grid(column=0,row=1)
botao_add_palavra = Button(janela,text="Adicionar palavra",command=add_palavra)
botao_add_palavra.grid(column=0,row=2)

janela.mainloop()
