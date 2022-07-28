from sorteia_palavra import sorteia_palavra
from oculta_palavra import oculta_palavra
from tabuleiro import tabuleiro

def jogar():
    palavra = sorteia_palavra()
    palavra_oculta = oculta_palavra()
    letras_erradas = []
    ultima_letra = ""
    tentativas = 0
    
    tabuleiro(tentativas, palavra, palavra_oculta, letras_erradas, ultima_letra)
