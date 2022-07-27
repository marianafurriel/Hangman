import random as r


def sorteiaTema(dicTemas):
    """Recebe um dicionario com temas de chave e lista de palavras como valor e retorna um desses temas, aleatoriamente e uma lista com as palavras do respectivo tema."""
    tema = r.choice(list(dicTemas))
    palavras = dicTemas.get(tema)
    indicesPalavras = []
    while(True):
        numeroAleatorio = r.randint(0, len(palavras)-1)
        if numeroAleatorio not in indicesPalavras:
            indicesPalavras = indicesPalavras + [numeroAleatorio]
        if len(indicesPalavras) == 3:
            break
    retorno = tema, [palavras[indicesPalavras[0]],
                     palavras[indicesPalavras[1]], palavras[indicesPalavras[2]]]
    return retorno
