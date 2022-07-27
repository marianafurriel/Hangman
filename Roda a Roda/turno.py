import roleta
import pedeLetra


def turno(pontos):
    jogador = 0
    while(jogador < 3):
        pontuacao = roleta.giraRoleta()
        if pontuacao == 'Passa a vez':
            jogador += 1
            continue
        elif pontuacao == 'Perdeu tudo':
            pontos[jogador] = 0
            jogador += 1
            continue
        else:
            pontos[jogador] = pontuacao
        letra = pedeLetra()
