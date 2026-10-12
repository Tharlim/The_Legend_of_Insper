"""Classe Chefe (herda de Inimigo): o boss do último nível.

O que é:
    Um inimigo maior, com muito mais vida e um jeito próprio de atacar.
    Quando ele morre, o jogador vence a partida.

Atributos:
    - nome: aparece no HUD (ex.: "Dragão Ancião").
    - fase: 1 ou 2. Muda para 2 quando a vida cai pela metade.

Métodos:
    - pensar(jogador): na fase 1 persegue devagar; na fase 2 fica mais
      rápido e, de tempos em tempos, atira projéteis em todas as direções.

Usa: personagens/projetil.py.
"""
