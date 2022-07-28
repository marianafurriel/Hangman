from ler_arquivo import ler_arquivo
from sorteia_elemento import sorteia_elemento


def sorteia_palavra():
    arquivo = ler_arquivo("palavras.txt")
    return sorteia_elemento(arquivo)
