def revela_letra(palavra, palavra_oculta, letra):
    if letra in palavra:
        for i in palavra:
            if palavra[i] == letra:
                palavra_oculta = palavra_oculta[:i]+letra+palavra_oculta[i+1:]

    return palavra_oculta
