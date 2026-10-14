"""Classe Jogador (herda de Entidade): o personagem controlado pelo teclado.

O que é:
    O Jogador anda pelo mapa do nível e ataca. A câmera segue ele. Ele TEM uma classe (Mago, Arqueiro
    ou Bárbaro) em vez de SER uma. Quando ataca, ele pede para a classe
    fazer o ataque. Assim, criar uma classe nova não exige mexer aqui.

Atributos:
    - classe: a ClasseHeroi escolhida.
    - direcao: para onde está virado (para mirar o ataque).
    - tempo_recarga: tempo até poder atacar de novo.

Métodos:
    - ler_teclado(): setas/WASD andam, ESPAÇO ataca, SHIFT usa o especial.
    - atacar(): chama classe.atacar(self) e devolve o que foi criado
      (projéteis ou o golpe) para o Nivel colocar no mapa.
    - especial(): mesma ideia, com classe.especial(self).
    - mover(dt, paredes): anda sem atravessar paredes.

Usa: personagens/classes/.
"""
import pygame
from personagens.entidade import Entidade


class Jogador(Entidade):
    def __init__(self, x, y, classe=None, velocidade=100):
        super().__init__(x, y, largura=16, altura=16, cor=(250, 210, 80))
        self.classe = classe
        self.velocidade = getattr(classe, "velocidade", velocidade)
        self.direcao = pygame.Vector2(0, 1)
        self.movimento = pygame.Vector2()

    def teclas(self, teclas=None):
        if teclas is None:
            teclas = pygame.key.get_pressed()

        self.movimento.update(
            int(teclas[pygame.K_d]) - int(teclas[pygame.K_a]),
            int(teclas[pygame.K_s]) - int(teclas[pygame.K_w]),
        )
        if self.movimento.length_squared() > 0:
            self.movimento.normalize_ip()
            self.direcao = self.movimento.copy()