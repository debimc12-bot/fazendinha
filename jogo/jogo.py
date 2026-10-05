import pygame

from configuracao.configuracao import Configuracao
from jogo.jogador import criar_jogador, mover_jogador
from jogo.terreno import criar_terrenos
from jogo.plantas import atualizar_planta
from jogo.corvo import criar_corvo, mover_corvo
from jogo.mala import criar_mala
from jogo.controle import processar_eventos
from jogo.desenhar import desenhar_jogo

def processar_ataque_corvo(resultado_corvo, vidas):
    if resultado_corvo == "atacou_jogador":
        vidas -= 1

        print("O corvo atacou o jogador!" f"Vidas restantes: {vidas}")

        if vidas <= 0:
            print("Fim de Jogo! O jogador perdeu todas as vidas")

            return vidas, Configuracao.FIM_DE_JOGO

    return vidas, Configuracao.JOGANDO

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

    vidas = config.vidas_iniciais

    jogador["tem_isca"] = False

    rodando = True

    while rodando:

        rodando, colhidas = processar_eventos(jogador, terrenos, mala)

        plantas_colhidas += colhidas

        if not rodando:
            break

        if estado == Configuracao.JOGANDO:

            teclas = pygame.key.get_pressed()

            mover_jogador(jogador, teclas)

            resultado_corvo = mover_corvo(corvo, terrenos, mala, jogador)

            if resultado_corvo == "planta_comida":

                plantas_comidas_corvo += 1
                print("O corvo comeu uma planta! Total de plantas comidas pelo corvo:" f"{plantas_comidas_corvo}")

            vidas, estado = processar_ataque_corvo(resultado_corvo, vidas)

        for terreno in terrenos:
            atualizar_planta(terreno["planta"])

        desenhar_jogo(tela, terrenos, jogador, corvo, mala, fonte, plantas_colhidas, vidas)

        pygame.display.flip()
        relogio.tick(config.fps)

    pygame.quit()