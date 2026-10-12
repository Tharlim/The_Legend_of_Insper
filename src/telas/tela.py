"""Classe Tela: o molde (classe base) de todas as telas.

O que é:
    Toda tela do jogo é uma classe que herda de Tela. Como todas têm os
    mesmos métodos, a Aplicacao consegue rodar qualquer uma sem saber qual
    é. Trocar de tela é só trocar o objeto.

Atributos:
    - aplicacao: a Aplicacao, para a tela poder trocar de tela e ler ou
      gravar os dados da partida.

Métodos (cada tela filha implementa os seus):
    - tratar_evento(evento): reage a uma tecla apertada ou letra digitada.
    - atualizar(dt): avança a lógica da tela. dt = segundos desde o último
      quadro (usar dt deixa a velocidade igual em PCs rápidos e lentos).
    - desenhar(superficie): desenha a tela.

Herdam dela: TelaInicial, TelaClasses, TelaJogo, TelaResultado.
"""
