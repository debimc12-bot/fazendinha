import pygame

from configuracao.configuracao import Configuracao
config = Configuracao()


def criar_planta():
    return {
        "estado": "semente",
        "tempo_plantio": pygame.time.get_ticks()
    }

def plantar(terreno):
    if terreno["planta"] is None:
        terreno["planta"] = criar_planta()
        return True

    return False

def colher(terreno):
    planta = terreno["planta"]

    if planta is not None and planta["estado"] == "pronta":
        terreno["planta"] = None
        return True

    return False

def atualizar_planta(planta):
    if planta is None:
        return

    tempo_atual = pygame.time.get_ticks()
    tempo_passado = (tempo_atual - planta["tempo_plantio"]) / 1000

    if tempo_passado >= config.tempo_crescimento:
        planta["estado"] = "pronta"
    
    elif tempo_passado >= config.tempo_crescimento / 2:
        planta["estado"] = "crescendo"


def desenhar_planta(tela, planta, terreno):
    if planta is None:
        return

    if planta["estado"] == "semente":
        cor = config.verde_semente
        tamanho = 12
    elif planta["estado"] == "crescendo":
        cor = config.verde_planta
        tamanho = 20
    elif planta["estado"] == "pronta":
        cor = config.verde_pronta
        tamanho = 30
    else:
        return

    planta_rect = pygame.Rect(terreno["rect"].centerx - tamanho // 2, terreno["rect"].centery - tamanho // 2, tamanho, tamanho)

    pygame.draw.rect(tela, cor, planta_rect)