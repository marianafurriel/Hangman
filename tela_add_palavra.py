from add_palavra import add_palavra
from tkinter import *
from janela_def import *

def tela_add_palavra():
    janela.title("Adicionar palavra")
    texto_orientacao = Label(janela, text="Insira a palavra")
    palavra = Text(janela)
    texto_orientacao.grid(column=0,row=0)    