"""Classe TelaResultado (herda de Tela): o fim da partida.

O que aparece:
    - VITÓRIA ou DERROTA.
    - Nome e classe do jogador.
    - Os pontos da partida (inimigos, níveis, chefe, bônus) e o total.
    - Em que posição ficou no ranking e o ranking ao lado.

O que faz:
    - Ao entrar: salva a partida no Ranking. Sempre salva, ganhando ou
      perdendo.
    - ENTER volta para TelaInicial. Se ninguém apertar nada por alguns
      segundos, volta sozinha (para o próximo visitante da feira).

Usa: jogo/ranking.py, ui/painel_ranking.py.
"""
