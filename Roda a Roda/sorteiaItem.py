import random as r


def sorteiaItem(lista):
    """Recebe uma lista e retorna um valor aleatório dessa lista"""
    tamanho = len(lista)
    indice = r.randint(0, len(lista)-1)
    return lista[indice]
