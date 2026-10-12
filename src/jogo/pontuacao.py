"""Classe Pontuacao: os pontos de uma partida.

O que é:
    Cada partida tem uma Pontuacao nova. O Mundo vai somando pontos
    durante o jogo e a TelaResultado mostra o total no fim.

Atributos:
    - total: os pontos somados até agora.
    - inimigos_derrotados: quantos inimigos o jogador matou.
    - extrato: lista com o motivo de cada ponto ("Nível 1 concluído +500"),
      mostrada na tela de resultado.

Métodos:
    - inimigo_derrotado(pontos): soma os pontos de um inimigo.
    - nivel_concluido(nome_nivel): soma os pontos de passar de nível.
    - chefe_derrotado(): soma os pontos do chefe.
    - aplicar_bonus(venceu, tempo, vida_restante): no fim da partida, se
      venceu, soma bônus por terminar rápido e por vida que sobrou.

Ideia de valores: inimigo 50 a 100, nível 500, chefe 2000.
Ganhando ou perdendo, o total vai para o ranking.

Quem usa: Mundo, TelaResultado.
"""
