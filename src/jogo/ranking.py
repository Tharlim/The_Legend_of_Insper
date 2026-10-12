"""Classe Ranking: o placar da feira.

O que é:
    Guarda todas as partidas num arquivo, para o ranking continuar lá
    mesmo depois de fechar o jogo.

Atributos:
    - caminho_arquivo: onde salvar (src/data/ranking.json).
    - partidas: lista com nome, classe, pontos e se venceu, em ordem do
      maior para o menor.

Métodos:
    - carregar(): lê o arquivo ao abrir o jogo. Se não existir ou estiver
      estragado, começa com a lista vazia (o jogo não pode travar na feira).
    - adicionar(nome, classe, pontos, venceu): coloca a partida na lista,
      ordena, salva e devolve a posição em que ficou.
    - melhores(quantidade): devolve os primeiros colocados.
    - salvar(): grava a lista no arquivo.

Quem usa: Aplicacao, TelaInicial, TelaResultado.
"""
