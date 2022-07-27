def revelaLetra(palavra, palavraOculta, letra):
    """Recebe 3 strings: uma palavra, a palavra oculta e uma letra. Retorna a palavra oculta com apenas a letra revelada em todas as posições que ela estiver na palavra."""
    if letra in palavra:
        aux = palavra.count(letra)
        for i in range(aux):
            indice = palavra.index(letra)
            palavraOculta = palavraOculta[:indice] + \
                letra + palavraOculta[indice+1:]
            palavra = palavra[:indice]+"$"+palavra[indice+1:]
    return palavraOculta
