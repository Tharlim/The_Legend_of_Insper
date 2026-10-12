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
