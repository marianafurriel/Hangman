from revela_letra import revela_letra
from sorteia_palavra import sorteia_palavra
from oculta_palavra import oculta_palavra
from tabuleiro import tabuleiro
from menu import menu


def jogar():
    palavra = sorteia_palavra()
    palavra_oculta = oculta_palavra(palavra)
    letras_erradas = []
    ultima_letra = ""
    palavra_tentada = ""
    tentativas = -1
    tabuleiro(tentativas, palavra, palavra_oculta,
              letras_erradas, ultima_letra)
    tentativas = 0
    while(True):
        option = menu(3)

        while((option != '1') and (option != '2') and (option != '3')):
            option = menu(3)

        if option == '1':
            print("Digite a letra: ")
            ultima_letra = input()
            if ultima_letra not in palavra:
                tentativas = tentativas+1
                letras_erradas.append(ultima_letra)
            else:
                palavra_oculta = revela_letra(
                    palavra, palavra_oculta, ultima_letra)
            if palavra_oculta == palavra:
                tabuleiro(tentativas, palavra, palavra_oculta,
                          letras_erradas, ultima_letra)
                break

        if option == '2':
            print('Digite a palavra que quer chutar: ')
            palavra_tentada = input()
            if palavra_tentada == palavra:
                palavra_oculta = palavra
                tabuleiro(tentativas, palavra, palavra_oculta,
                          letras_erradas, ultima_letra)
                break

        if option == '3':
            palavra_oculta = palavra
            tabuleiro(tentativas, palavra, palavra_oculta,
                      letras_erradas, ultima_letra)
            break

        tabuleiro(tentativas, palavra, palavra_oculta,
                  letras_erradas, ultima_letra)
