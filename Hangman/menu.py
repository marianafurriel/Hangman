def menu(menu):
    if menu == 1:
        print("Olá! O que deseja fazer? Digite a opção desejada:")
        print("1 - Jogar\n2 - Adicionar palavra\n3 - Sair")
        option = input()

    elif menu == 2:
        print("Digite uma opção válida!")
        print("1 - Jogar\n2 - Adicionar palavra\n3 - Sair")
        option = input()

    elif menu == 3:
        print("O que deseja fazer?\n1 - Tentar uma letra\n 2 - Chutar a palavra\n3 - Mostrar a palavra\n")
        option = input()
        
    return option
