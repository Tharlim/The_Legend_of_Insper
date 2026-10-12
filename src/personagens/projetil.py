"""Classe Projetil (herda de Entidade): o que voa e dá dano.

Exemplos: flecha do arqueiro, bola de fogo do mago, tiro do chefe.

Atributos:
    - direcao e velocidade: para onde e quão rápido voa.
    - dano: quanto tira de vida.
    - dono: "jogador" ou "inimigo", para não acertar o próprio lado.

Métodos:
    - atualizar(dt): anda em linha reta.
    - Some quando bate numa parede ou acerta alguém (o Nivel cuida disso).
"""
