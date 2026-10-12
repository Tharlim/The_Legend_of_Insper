"""Classe CaixaTexto: campo para digitar o nome do jogador.

O que é:
    Um retângulo na tela onde aparece o que o jogador digita, com um
    cursor piscando no final.

Atributos:
    - texto: o que já foi digitado.
    - tamanho_maximo: quantas letras cabem no nome.
    - retangulo: posição e tamanho da caixa na tela.

Métodos:
    - tratar_evento(evento): adiciona a letra digitada ou apaga com
      backspace. Ignora caracteres estranhos.
    - desenhar(superficie): desenha a caixa, o texto e o cursor.

Usada em: TelaInicial.
"""
