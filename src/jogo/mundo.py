"""Classe Mundo: o mundo inteiro da partida, com os 3 níveis.

O que é:
    O Mundo é quem controla o jogo durante a partida. Ele é criado a partir
    do tema (torre, Insper ou dungeon), monta os 3 Niveis e decide quando
    passar para o próximo, quando o jogador venceu e quando perdeu.
    A TelaJogo só conversa com o Mundo, nunca direto com um Nivel.

Atributos (o que ele guarda):
    - tema: o tema escolhido (vem de jogo/temas.py).
    - niveis: lista com os 3 Niveis, na ordem em que são jogados.
    - indice_nivel: qual nível está sendo jogado agora (0, 1 ou 2).
    - jogador: o Jogador, que passa de um nível para o outro com a vida
      que sobrou.
    - pontuacao: a Pontuacao da partida, que ele vai somando.
    - camera: a Camera que segue o jogador pelo nível atual.
    - venceu: True quando o chefe morre.

Métodos (o que ele faz):
    - nivel_atual(): devolve o Nivel que está sendo jogado.
    - atualizar(dt): atualiza o nível atual, faz a câmera seguir o jogador
      e aplica as regras:
        * inimigo morreu -> soma os pontos dele;
        * nível 1 ou 2 limpo e jogador na saída -> soma pontos do nível e
          avança para o próximo (proximo_nivel);
        * chefe morreu -> soma pontos do chefe e marca venceu;
        * vida do jogador zerou -> a partida acaba em derrota.
    - proximo_nivel(): avança indice_nivel, coloca o jogador no início do
      novo nível e avisa a câmera do tamanho do novo mapa.
    - terminou(): True se venceu ou se o jogador morreu.
    - desenhar(superficie): desenha o nível atual através da câmera.

Quem usa: TelaJogo.
Usa: jogo/nivel.py, jogo/camera.py, jogo/temas.py, jogo/pontuacao.py.
"""
