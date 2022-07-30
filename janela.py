from tkinter import *
from janela_def import *
from jogar import jogar
from tela_add_palavra import tela_add_palavra

janela.title("Hangman")
texto_orientacao = Label(janela, text="Bem vindo! O que deseja fazer?")
texto_orientacao.grid(column=0,row=0)

botao_jogar = Button(janela,text="Jogar",command=jogar)
botao_jogar.grid(column=0,row=1)
botao_add_palavra = Button(janela,text="Adicionar palavra",command=tela_add_palavra)
botao_add_palavra.grid(column=0,row=2)

janela.mainloop()
