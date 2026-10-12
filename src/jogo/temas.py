"""temas.py: os temas do jogo e os níveis de cada um.

O que é:
    Só dados, sem lógica. O tema ainda não foi decidido (torre, Insper ou
    dungeon), então todos ficam descritos aqui e o Mundo usa o escolhido.

O que guarda para cada tema:
    - nome (ex.: "Subindo a Torre");
    - direção: se o jogador sobe ou desce;
    - os 3 níveis, cada um com:
        * nome (ex.: "Biblioteca");
        * tamanho do mapa (ex.: 3 telas de largura por 2 de altura);
        * cores do chão e da parede (ou o tileset, quando tiver arte);
        * quais inimigos aparecem e quantos de cada;
    - qual chefe aparece no último nível.

Trocar de tema = escolher outro tema daqui (sem mexer em nenhuma classe).

Quem usa: Mundo.
"""
