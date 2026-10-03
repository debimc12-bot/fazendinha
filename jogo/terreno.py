import pygame

from configuracao.configuracao import Configuracao
config = Configuracao()

def criar_terrenos():
    terrenos = []

    for linha in range(config.quantidade_linhas):
        for coluna in range(config.quantidade_colunas):
            x = config.terreno_x + coluna * config.tamanho_terreno
            y = config.terreno_y + linha * config.tamanho_terreno

            terreno = {
                "rect": pygame.Rect (x, y, config.tamanho_terreno, config.tamanho_terreno),
                "planta": None
            }

            terrenos.append(terreno)

    return terrenos

def desenhar_terrenos(tela, terrenos):
    for terreno in terrenos:
        pygame.draw.rect(tela, config.marrom_terra, terreno["rect"])
        pygame.draw.rect(tela, (80, 50, 25), terreno["rect"], 2)