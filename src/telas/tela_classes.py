"""Classe TelaClasses (herda de Tela): escolha da classe.

O que aparece:
    Três cartões lado a lado: Mago, Arqueiro e Bárbaro, cada um com
    imagem, nome e atributos. O cartão selecionado fica destacado, e
    embaixo aparece a descrição da classe selecionada.

Atributos:
    - cartoes: lista com um CartaoClasse para cada classe.
    - selecionado: índice da classe destacada (0, 1 ou 2).

O que faz:
    - Setas esquerda/direita: mudam o selecionado.
    - ENTER: guarda a classe em aplicacao.classe_escolhida e troca para
      TelaJogo.
    - ESC: volta para TelaInicial.

Usa: ui/cartao_classe.py, personagens/classes/.
"""
