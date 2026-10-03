import pygame

from configuracao.configuracao import (MARROM_TERRA, TAMANHO_TERRENO, TERRENO_X, TERRENO_Y, QUANTIDADE_COLUNAS, QUANTIDADE_LINHAS)

def criar_terrenos():
    terrenos = []

    for linha in range(QUANTIDADE_LINHAS):
        for coluna in range(QUANTIDADE_COLUNAS):
            x = TERRENO_X + coluna * TAMANHO_TERRENO
            y = TERRENO_Y + linha * TAMANHO_TERRENO

            terreno = {
                "rect": pygame.Rect (x, y, TAMANHO_TERRENO, TAMANHO_TERRENO),
                "planta": None
            }

            terrenos.append(terreno)

    return terrenos

def desenhar_terrenos(tela, terrenos):
    for terreno in terrenos:
        pygame.draw.rect(tela, MARROM_TERRA, terreno["rect"])
        pygame.draw.rect(tela, (80, 50, 25), terreno["rect"], 2)