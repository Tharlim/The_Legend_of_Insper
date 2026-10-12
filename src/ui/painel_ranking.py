"""Classe PainelRanking: o quadro que mostra o ranking.

O que é:
    Só desenha. Não lê nem salva arquivo; quem faz isso é o Ranking.

Atributos:
    - retangulo: posição e tamanho do quadro na tela.

Métodos:
    - desenhar(superficie, lista, destaque): desenha título e uma linha por
      jogador (posição, nome, pontos). Se receber um destaque, pinta essa
      linha de outra cor (quem acabou de jogar).

Usada em: TelaInicial e TelaResultado.
"""
