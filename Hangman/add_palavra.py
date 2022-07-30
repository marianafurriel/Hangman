from ler_arquivo import ler_arquivo
from escrever_arquivo import escrever_arquivo


def add_palavra():
    print("Digite a palavra que quer adicionar:")
    palavra = input()
    palavra = palavra+"\n"
    option = 's'
    while(option != 'n'):
        if palavra not in ler_arquivo():
            escrever_arquivo(palavra)
        else:
            print("Essa palavra já foi adicionada, deseja tentar novamente?(s/n)")
            option = input()
    return
