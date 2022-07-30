from jogar import jogar
from add_palavra import add_palavra
from menu import menu


def main():
    option = 0
    while(option != '3'):
        option = menu(1)

        while((option != '1') and (option != '2') and (option != '3')):
            option = menu(1)

        if option == '1':
            jogar()
        elif option == '2':
            add_palavra()


if __name__ == "__main__":
    main()
