"""Classe Entidade: a base de tudo que aparece dentro de um nível.

O que é:
    Jogador, inimigos, chefe e projéteis têm várias coisas em comum
    (posição, imagem, vida). Em vez de repetir isso em cada classe,
    fica tudo aqui e as outras herdam.

Atributos:
    - x, y: posição no mapa do nível (não na tela).
    - retangulo: área usada para ver se encostou em algo (colisão).
    - imagem: o sprite (enquanto não tiver arte, um quadrado colorido).
    - vida: quanto dano ainda aguenta.

Métodos:
    - receber_dano(quantidade): diminui a vida. Após levar dano, fica
      alguns instantes sem levar dano de novo (pisca na tela).
    - esta_vivo(): True enquanto vida > 0.
    - atualizar(dt): cada filha define o que faz a cada quadro.
    - desenhar(superficie, camera): pede para a câmera converter a posição
      do mapa em posição na tela e desenha a imagem ali.

Herdam dela: Jogador, Inimigo (e Chefe) e Projetil.
"""
import pygame


class Entidade:
    def __init__(self, x, y, largura=16, altura=16, cor=(240, 240, 232), vida=1):
        # A posição em float preserva movimentos menores que um pixel por quadro.
        self.x = float(x)
        self.y = float(y)
        self.retangulo = pygame.Rect(round(x), round(y), largura, altura)
        self.imagem = pygame.Surface((largura, altura))
        self.imagem.fill(cor)
        self.vida = vida