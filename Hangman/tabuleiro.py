from bonecos import bonecos


def tabuleiro(tentativas, palavra, palavra_oculta, letras_erradas=[], ultima_letra=""):
    """Função que recebe a quantidade de tentativas, a palavra correta, a palavra oculta, as letras erradas e a última letra tentada pelo usuário e imprime o tabuleiro de acordo com a situação atual do jogo."""
    if (ultima_letra in palavra):  # a letra tentada está na palavra
        if(palavra_oculta == palavra):  # palavra oculta já está descoberta
            print("\t\tAcertou a palavra!")
            print(bonecos[tentativas])
            print("\t\t", palavra_oculta.upper())
        else:
            print("\t\tAcertou a letra!")
            print(bonecos[tentativas])
            exibicao_oculta = " ".join(list(palavra_oculta))
            print("\t\t", exibicao_oculta.upper())
            print("\n\tLetras erradas: ", str(letras_erradas))

    elif(palavra_oculta == palavra):  # palavra oculta já está descoberta
        print("\t\tA palavra era")
        print(bonecos[tentativas])
        print("\t\t", palavra_oculta.upper())

    elif(tentativas == -1):  # tabuleiro inicial
        print("\t\tBem-vindo!")
        print(bonecos[0])
        exibicao_oculta = " ".join(list(palavra_oculta))
        print("\t\t", exibicao_oculta)

    elif(tentativas == 6):  # segunda perna adicionada ao boneco, fim de jogo
        print("\t\tVocê perdeu!")
        print(bonecos[6])
        print("\t\t", palavra.upper())
        print("\n\tLetras erradas: ", str(letras_erradas))


    else:  # a letra tentada não está na palavra
        print("\tErrou a letra!")
        print(bonecos[tentativas])
        exibicao_oculta = " ".join(list(palavra_oculta))
        print("\t\t", exibicao_oculta.upper())
        print("\n\tLetras erradas: ", ' '.join(letras_erradas))
