from jogar import jogar 
from add_palavra import add_palavra

def main():
    print("Olá! O que deseja fazer? Digite a opção desejada:")
    print("1 - Jogar\n2 - Adicionar palavra")
    option = input()

    while(option!=1)and(option!=2):
        print("Digite uma opção válida!")
        print("1 - Jogar\n2 - Adicionar palavra")
        option = input()

    if option == 1:
        add_palavra()
    else:
        jogar()
    