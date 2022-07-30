def escrever_arquivo(palavra):
    arquivo = open("palavras.txt", "a")
    arquivo.write(palavra)
