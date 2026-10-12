"""Classe Nivel: um nível (andar) do jogo.

O que é:
    Um mapa grande, maior que a tela, como nos Pokémon antigos. A tela
    mostra só um pedaço dele por vez, através da Camera. Tem paredes,
    inimigos espalhados e uma saída (escada ou porta) para o próximo nível.
    Cada nível tem um estilo diferente (cores, inimigos, tamanho), que vem
    do tema. O Mundo cria 3 Niveis e joga um de cada vez.

Atributos:
    - nome: nome do nível (ex.: "Catacumbas").
    - numero: 1, 2 ou 3.
    - largura, altura: tamanho do mapa em pixels (maior que a tela).
    - mapa: grade de tiles (quadradinhos de 16x16) dizendo onde é chão e
      onde é parede. Pode ser desenhado num editor como o Tiled depois.
    - paredes: lista de retângulos por onde ninguém passa.
    - inimigos: lista de Inimigos vivos no nível.
    - chefe: o Chefe (só existe no nível 3).
    - projeteis: flechas, bolas de fogo e tiros voando agora.
    - saida: retângulo da porta/escada. Só abre quando todos os inimigos morrem.
    - posicao_inicial: onde o jogador aparece ao entrar.
    - cores: cor do chão e das paredes (até ter sprites).

Métodos:
    - atualizar(dt, jogador): move inimigos e projéteis e checa colisões:
        * ataque do jogador encostou num inimigo -> inimigo leva dano;
        * inimigo ou tiro do chefe encostou no jogador -> jogador leva dano;
        * projétil bateu na parede -> some.
    - remover_mortos(): tira do nível os inimigos com vida zero e devolve
      quem morreu (para o Mundo somar os pontos).
    - esta_limpo(): True quando não sobrou nenhum inimigo.
    - jogador_na_saida(jogador): True quando o jogador encosta na saída.
    - desenhar(superficie, camera): desenha só o pedaço do mapa que a
      câmera está mostrando, com a saída e todo mundo que estiver visível.

Quem usa: Mundo.
Usa: personagens/.
"""
