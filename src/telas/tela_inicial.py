"""Classe TelaInicial (herda de Tela): a primeira tela do jogo.

O que aparece:
    - À esquerda: nome do jogo e um campo para digitar o nome do jogador.
    - À direita: o ranking com os melhores jogadores.
    - Embaixo: "ENTER para jogar".

Atributos:
    - caixa_nome: CaixaTexto onde o jogador digita o nome.
    - painel_ranking: PainelRanking que desenha a lista.

O que faz:
    - tratar_evento: passa as letras digitadas para a caixa_nome.
    - atualizar: se apertou ENTER e o nome não está vazio, chama
      aplicacao.nova_partida(nome) e troca para TelaClasses.
      Se o nome estiver vazio, mostra um aviso.
    - desenhar: título, caixa de nome e ranking.

Usa: ui/caixa_texto.py, ui/painel_ranking.py, jogo/ranking.py.
"""
