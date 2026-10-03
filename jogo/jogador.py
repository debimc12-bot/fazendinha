import pygame

from configuracao.configuracao import (TAMANHO_JOGADOR, VELOCIDADE_JOGADOR, BRANCO, LARGURA_TELA, ALTURA_TELA)

def criar_jogador():
    return {
        "x": LARGURA_TELA // 2,
        "y": ALTURA_TELA // 2
    }

def mover_jogador(jogador, teclas):
    if teclas[pygame.K_LEFT]:
        jogador["x"] -= VELOCIDADE_JOGADOR

    if teclas[pygame.K_RIGHT]:
        jogador["x"] += VELOCIDADE_JOGADOR

    if teclas[pygame.K_UP]:
        jogador["y"] -= VELOCIDADE_JOGADOR

    if teclas[pygame.K_DOWN]:
        jogador["y"] += VELOCIDADE_JOGADOR

   
    jogador["x"] = max(0, min(jogador["x"], LARGURA_TELA - TAMANHO_JOGADOR))

    jogador["y"] = max(0, min(jogador["y"], ALTURA_TELA - TAMANHO_JOGADOR))


def desenhar_jogador(tela, jogador):
    jogador_rect = pygame.Rect(jogador["x"], jogador["y"], TAMANHO_JOGADOR, TAMANHO_JOGADOR)

    pygame.draw.rect(tela, BRANCO, jogador_rect)