import pygame

from configuracao.configuracao import Configuracao
from jogo.jogador import (criar_jogador, mover_jogador, desenhar_jogador)
from jogo.terreno import (criar_terrenos, desenhar_terrenos)
from jogo.plantas import (plantar, colher, atualizar_planta, desenhar_planta)
from jogo.corvo import (criar_corvo, mover_corvo, desenhar_corvo)
from jogo.mala import (criar_mala, pegar_isca, desenhar_mala, jogar_isca, desenhar_isca)

def iniciar_jogo():
    pygame.init()

    config = Configuracao()

    estado = Configuracao.MENU
    
    tela = pygame.display.set_mode((config.largura_tela, config.altura_tela))
    pygame.display.set_caption(config.titulo_jogo)

    relogio = pygame.time.Clock()

    fonte = pygame.font.SysFont(None, 32)
    plantas_colhidas = 0 

    jogador = criar_jogador()
    terrenos = criar_terrenos()
    corvo = criar_corvo()
    mala = criar_mala()
    jogador["tem_isca"] = False

    rodando = True

    while rodando:
        if estado == Configuracao.MENU:
            print("Abrindo Menu")
            estado = Configuracao.JOGANDO
        
        elif estado == Configuracao.JOGANDO:
            print("Jogando")

        elif estado == Configuracao.PAUSADO:
            print("Jogo Pausado")
            
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_e:
                    pegou = pegar_isca(mala, jogador)

                    if pegou:
                        print("Voce pegou uma isca!")
                    else:
                        for terreno in terrenos:
                            if terreno["rect"].collidepoint(jogador["x"] + 15, jogador["y"] + 15):
                                if terreno["planta"] is None:
                                    plantar(terreno)
                                elif colher(terreno):
                                    plantas_colhidas += 1
                                        
                                break

                if evento.key == pygame.K_q:
                     if jogar_isca(mala, jogador):
                         print("Voce jogou a isca!")
                     else:
                         print("Voce nao tem isca para jogar.")

        teclas = pygame.key.get_pressed()
        mover_jogador(jogador, teclas)
        mover_corvo(corvo, terrenos, mala)

        tela.fill(config.verde_grama)

        texto_colheita = fonte.render(f"Plantas colhidas: {plantas_colhidas}", True, (255, 255, 255))
        tela.blit(texto_colheita, (20, 20))

        desenhar_terrenos(tela, terrenos)

        for terreno in terrenos:
            atualizar_planta(terreno["planta"])
            desenhar_planta(tela, terreno["planta"], terreno)

        desenhar_jogador(tela, jogador)
        desenhar_corvo(tela, corvo)

        desenhar_mala(tela, mala)
        desenhar_isca(tela, mala)

        pygame.display.flip()
        relogio.tick(config.fps)

    pygame.quit()