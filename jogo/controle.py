import pygame

from configuracao.configuracao import Configuracao
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

def processar_tecla(evento, jogador, terrenos, mala, estado):

    if evento.key == pygame.K_ESCAPE:
    
            if estado == Configuracao.JOGANDO:
                estado = Configuracao.PAUSADO
    
            elif estado == Configuracao.PAUSADO:
                estado = Configuracao.JOGANDO
            return 0, estado

    if estado == Configuracao.PAUSADO:
        return 0, estado

    if evento.key == pygame.K_e:
        return (pressionar_e(jogador, terrenos, mala), estado)

    if evento.key == pygame.K_q:
        pressionar_q(jogador, mala)

        return 0, estado
    
    return 0, estado

def processar_eventos(jogador, terrenos, mala, estado):
    plantas_colhidas = 0

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            return False, plantas_colhidas, estado
        
        if evento.type == pygame.KEYDOWN:
            colhidas, estado = processar_tecla(evento, jogador, terrenos, mala, estado)
            plantas_colhidas += colhidas

    return True, plantas_colhidas, estado