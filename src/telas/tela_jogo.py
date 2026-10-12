"""Classe TelaJogo (herda de Tela): a tela onde se joga.

O que é:
    Uma tela "fina": quem controla os níveis é o Mundo. A TelaJogo só cria
    o Mundo, repassa o teclado, desenha e decide quando a partida acabou.

Atributos:
    - jogador: o Jogador, criado com a classe escolhida.
    - mundo: o Mundo, com os 3 níveis do tema escolhido.
    - hud: o Hud desenhado por cima do jogo.

O que faz:
    - Ao entrar: cria o Jogador e o Mundo.
    - atualizar(dt): chama mundo.atualizar(dt). Se mundo.terminou(),
      troca para TelaResultado (ganhando ou perdendo).
    - desenhar: desenha o mundo (só o pedaço que a câmera mostra) e o HUD
      por cima, fixo na tela. Ao trocar de nível,
      mostra o nome do nível no meio da tela por uns segundos.

Usa: jogo/mundo.py, personagens/jogador.py, ui/hud.py.
"""
