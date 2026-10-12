"""Classe Inimigo (herda de Entidade): os inimigos comuns.

O que é:
    Andam em direção ao jogador e dão dano quando encostam nele.
    Cada tipo de inimigo muda só os números e a imagem.

Atributos:
    - velocidade: quão rápido anda.
    - dano_contato: quanto dano dá ao encostar no jogador.
    - pontos: quanto vale quando morre.

Métodos:
    - pensar(jogador): decide para onde andar. IA simples: fica parado ou
      vagando até o jogador chegar perto, e então vai na direção dele.
    - atualizar(dt): pensa e anda sem atravessar paredes.

Tipos sugeridos (subclasses aqui mesmo):
    - Slime: lento, pouca vida.
    - Esqueleto: velocidade média, mais vida.
    - Morcego: rápido, pouca vida, voa em zigue-zague.

Herda dela: Chefe.
"""
