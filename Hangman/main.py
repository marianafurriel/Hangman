from jogar import jogar
from add_palavra import add_palavra


def main():
    print("Olá! O que deseja fazer? Digite a opção desejada:")
    print("1 - Jogar\n2 - Adicionar palavra\n3 - Sair")
    option = input()

    while((option != '1') and (option != '2') and (option != '3')):
        print("Digite uma opção válida!")
        print("1 - Jogar\n2 - Adicionar palavra\n3 - Sair")
        option = input()

    if option == '1':
        jogar()
    elif option == '2':
        add_palavra()


main()
