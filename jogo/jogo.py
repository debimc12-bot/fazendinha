import pygame

from configuracao.configuracao import Configuracao
from jogo.jogador import (criar_jogador, mover_jogador, desenhar_jogador)
from jogo.terreno import (criar_terrenos, desenhar_terrenos)
from jogo.plantas import (plantar, colher, atualizar_planta, desenhar_planta)
from jogo.corvo import (criar_corvo, mover_corvo, desenhar_corvo)
from jogo.mala import (criar_mala, pegar_isca, desenhar_mala, jogar_isca, desenhar_isca)

def processar_eventos(jogador, terrenos, mala):
    plantas_colhidas = 0

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            return False, plantas_colhidas
        
        if evento.type == pygame.KEYDOW:
            if evento.key == pygame.K_e:
                pegou = pegar_isca(mala, jogador)

                if pegou:
                    print("Pegou a isca!")
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
                    print("Jogo a isca!")
                else:
                    print("Sem isca para jogar!")

    return True, plantas_colhidas

def iniciar_jogo():
    pygame.init()

    config = Configuracao()
    estado = Configuracao.JOGANDO

    tela = pygame.display.set_mode((config.largura_tela, config.altura_tela))
    pygame.display.set_caption(config.titulo_jogo)

    relogio = pygame.time.Clock()

    fonte = pygame.font.SysFont(None, 32)

    plantas_colhidas = 0
    plantas_comidas_corvo = 0

    jogador = criar_jogador()
    terrenos = criar_terrenos()
    corvo = criar_corvo()
    mala = criar_mala()

    jogador["tem_isca"] = False

    rodando = True

    while rodando:
        rodando, colhidas = processar_eventos(jogador, terrenos, mala)

        plantas_colhidas += colhidas
        if not rodando:
            break

        if estado == Configuracao.JOGANDO:

            teclas = pygame.key.get_prossed()

            mover_jogador(jogador, teclas)
            comeu = mover_corvo(corvo, terrenos, mala)

            if comeu:
                plantas_comidas_corvo += 1
                print(f"O corvo comeu uma planta!"
                      f"Total de plantas comidas: {plantas_comidas_corvo}")

            if plantas_comidas_corvo >= 10:
                estado = Configuracao.FIM_DE_JOGO
                print("Fim de jogo! O corvo comeu muitas plantas.")
                continue

        tela.fill(config.verde_grama)

        texto_colheita = fonte.render(f"Plantas colhidas: {plantas_colhidas}", True, config.cor_texto)
        tela.blit(texto_colheita, (20, 20))

        desenhar_terrenos(tela, terrenos)
        for terreno in terrenos:
            atualizar_planta(terreno["planta"])

            desenhar_planta(tela, terreno["planta"], terreno)
            desenhar_jogador(tela, jogador)
            desenhar_corvo(tela, corvo)
            desenhar_mala(tela, mala)
            desenhar_isca(tela, mala)

            pygame.diplay.flip()
            relogio.tick(config.fps)

            pygame.quit()






