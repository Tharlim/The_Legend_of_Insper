"""Classe ClasseHeroi: o molde (classe base) das classes jogáveis.

O que é:
    Define o que toda classe jogável precisa ter. O Jogador guarda uma
    ClasseHeroi e pede para ela atacar, sem saber qual classe é.

Atributos (cada classe filha define os seus valores):
    - nome e descricao: aparecem na tela de escolha.
    - vida_maxima, velocidade, dano.
    - tempo_entre_ataques e tempo_entre_especiais.

Métodos:
    - atacar(jogador): o ataque básico. Devolve o que o ataque cria
      (projéteis ou um golpe corpo a corpo).
    - especial(jogador): a habilidade especial, mesma ideia.

Herdam dela: Mago, Arqueiro e Barbaro.
"""
