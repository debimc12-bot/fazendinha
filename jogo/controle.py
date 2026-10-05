import pygame

from jogo.plantas import plantar, colher
from jogo.mala import pegar_isca, jogar_isca

def interagir_com_terreno(jogador, terrenos):
    for terreno in terrenos:

        if terreno["rect"].collidepoint(
            jogador["x"] + 15,
            jogador["y"] + 15
        ):

            if terreno["planta"] is None:
                plantar(terreno)

            elif colher(terreno):
                return 1

            break

    return 0

def pressionar_e(jogador, terrenos, mala):
    pegou = pegar_isca(mala, jogador)

    if pegou:
        print("Pegou a isca!")
        return 0

    return interagir_com_terreno(jogador, terrenos)

def pressionar_q(jogador, mala):
    if jogar_isca(mala, jogador):
        print("Jogou a isca!")
    else:
        print("Sem isca para jogar!")

def processar_tecla(evento, jogador, terrenos, mala):

    if evento.key == pygame.K_e:
        return pressionar_e(jogador, terrenos, mala)

    if evento.key == pygame.K_q:
        pressionar_q(jogador, mala)
        return 0
    
    return 0

def processar_eventos(jogador, terrenos, mala):
    plantas_colhidas = 0

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            return False, plantas_colhidas
        
        if evento.type == pygame.KEYDOWN:
            plantas_colhidas += processar_tecla(evento, jogador, terrenos, mala)

    return True, plantas_colhidas