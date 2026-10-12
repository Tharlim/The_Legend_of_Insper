"""Classe Camera: mostra só o pedaço do nível em volta do jogador.

O que é:
    Os níveis são maiores que a tela, como nos Pokémon antigos. A tela
    mostra só um "recorte" do mapa, e esse recorte acompanha o jogador
    enquanto ele anda. A Camera é quem sabe onde esse recorte está.

Atributos:
    - x, y: canto superior esquerdo do recorte, em coordenadas do mapa.
    - largura, altura: tamanho do recorte (o tamanho da tela do jogo).
    - largura_mapa, altura_mapa: tamanho do nível atual, para a câmera
      não mostrar nada fora do mapa.

Métodos:
    - seguir(jogador): centraliza o recorte no jogador. Perto das bordas do
      mapa, a câmera para e quem anda na tela é o jogador.
    - para_tela(retangulo): converte uma posição do mapa para a posição na
      tela (posição no mapa menos x, y da câmera). Todo mundo que desenha
      dentro do nível usa isso.
    - esta_visivel(retangulo): True se algo está dentro do recorte. Serve
      para não desenhar o que está fora da tela.
    - mudar_mapa(largura, altura): chamado ao trocar de nível, porque cada
      nível pode ter um tamanho diferente.

O HUD não usa a câmera: ele fica sempre no mesmo lugar da tela.

Quem usa: Mundo (atualiza), Nivel e Entidade (para desenhar).
"""
