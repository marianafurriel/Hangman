def tabuleiro(pontos, jogador, roleta, pontosAtuais, tema, p1, p2, p3, letrasErradas):
    print(
        f"+= == == == == == == == == == == == == == == == == == == == == == == ===\n| RODADA X - TURNO Y\n+= == == == == == == == == == == == == == == == == == == == == == == ===\n| ANA - {pontos['Ana']} | BARBARA - {pontos['Bárbara']} | CARLOS - {pontos['Carlos']}\n+= == == == == == == == == == == == == == == == == == == == == == == ===\nJogador ativo: {jogador}\nPontuação atual: {pontos[jogador]}>\nRoleta: {roleta}\nNova pontuacao: {pontosAtuais}\n+= == == == == == == == == == == == == == == == == == == == == == == ===\nTema: {tema}\nP1) {p1}\nP2){p2}\nP3){p3}\nLetras erradas: {letrasErradas}\n+= == == == == == == == == == == == == == == == == == == == == == == == =")


#tabuleiro({'Ana': 100, 'Bárbara': 150, 'Carlos': 0}, 'Ana', '100',
          300, 'Animais', '_ a _', '_ a _ _', '_ a _ a _ _', ['z', 'h'])
