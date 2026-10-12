"""Classe Aplicacao: o "motor" que mantém o jogo rodando.

O que é:
    Existe uma única Aplicacao durante todo o programa. Ela abre a janela,
    roda o loop principal e sabe qual tela está aparecendo agora.
    Também guarda os dados da partida que precisam passar de uma tela
    para outra (o nome digitado na primeira tela é usado na última).

Atributos (o que ela guarda):
    - janela: a janela do pygame.
    - relogio: controla o FPS (quantos quadros por segundo).
    - tela_atual: a Tela que está ativa (TelaInicial, TelaJogo...).
    - ranking: o objeto Ranking, criado uma vez e usado pelas telas.
    - nome_jogador: nome digitado na TelaInicial.
    - classe_escolhida: classe escolhida na TelaClasses (Mago, Arqueiro...).
    - pontuacao: a Pontuacao da partida atual.

Métodos (o que ela faz):
    - executar(): loop principal. A cada quadro:
        1. lê os eventos do teclado e repassa para tela_atual;
        2. chama tela_atual.atualizar(dt);
        3. chama tela_atual.desenhar(...) e mostra na janela.
    - trocar_tela(nova_tela): troca a tela ativa (ex.: da inicial para a
      de escolha de classe).
    - nova_partida(nome): limpa os dados da partida anterior e guarda o nome.

Quem usa: main.py.
Usa: telas/, jogo/ranking.py, jogo/pontuacao.py.
"""
