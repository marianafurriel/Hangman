def ler_arquivo(nome):
    """Função que recebe o nome do arquivo em uma string no formato 'nome.extensao' e retorna uma lista onde cada elemento é uma linha do arquivo."""
    arquivo = open(nome, 'r')
    return arquivo.readlines()
