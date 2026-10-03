import pygame

from configuracao.configuracao import Configuracao
config = Configuracao()
TAMANHO_CORVO = 30
VELOCIDADE_CORVO = 2
COR_CORVO = (25, 25, 25)
TEMPO_COMENDO = 1000  

def criar_corvo():
    return {
        "x": config.largura_tela - 80,
        "y": 80,
        "alvo_x": config.largura_tela - 80,
        "alvo_y": 80,
        "estado": "vigiando",
        "tempo_comecou_comer": 0
    }

def mover_corvo(corvo, terrenos, mala):
    
    if corvo["estado"] == "comendo":
        tempo_atual = pygame.time.get_ticks()

        if tempo_atual - corvo["tempo_comecou_comer"] >= TEMPO_COMENDO:
            terreno = corvo["terreno_alvo"]
            terreno["planta"] = None

            corvo["estado"] = "vigiando"
            corvo.pop("terreno_alvo")

        return

    if mala["isca_no_chao"]:
        alvo_x = mala["isca_x"]
        alvo_y = mala["isca_y"]

        dx = alvo_x - (corvo["x"] + 15)
        dy = alvo_y - (corvo["y"] + 15)
        distancia = (dx ** 2 + dy ** 2) ** 0.5

        if distancia <= 5:
            mala["isca_no_chao"] = False
            corvo["estado"] = "parado"
        else:
            corvo["x"] += (dx / distancia) * 2
            corvo["y"] += (dy / distancia) * 2

        return

    plantas_maduras = [terreno for terreno in terrenos if terreno["planta"] is not None and terreno["planta"]["estado"] == "pronta"]

    if plantas_maduras:
        
        terreno_alvo = min(plantas_maduras, key=lambda terreno: pygame.Vector2(corvo["x"] + TAMANHO_CORVO / 2, corvo["y"] + TAMANHO_CORVO / 2).distance_to(terreno["rect"].center))

        corvo["estado"] = "caçando"
        corvo["terreno_alvo"] = terreno_alvo
        corvo["alvo_x"] = terreno_alvo["rect"].centerx - TAMANHO_CORVO / 2
        corvo["alvo_y"] = terreno_alvo["rect"].centery - TAMANHO_CORVO / 2

    else:
        corvo["estado"] = "vigiando"

        
        if (corvo["alvo_x"] == config.largura_tela - 80 and corvo["alvo_y"] == 80):
            corvo["alvo_x"] = config.largura_tela - 250
            corvo["alvo_y"] = 80

        elif (corvo["alvo_x"] == config.largura_tela - 250 and corvo["alvo_y"] == 80):
            corvo["alvo_x"] = config.largura_tela - 80
            corvo["alvo_y"] = 80
    
    diferenca_x = corvo["alvo_x"] - corvo["x"]
    diferenca_y = corvo["alvo_y"] - corvo["y"]

    distancia = pygame.Vector2(diferenca_x, diferenca_y).length()

    if distancia > VELOCIDADE_CORVO:
        direcao = pygame.Vector2(diferenca_x, diferenca_y).normalize()

        corvo["x"] += direcao.x * VELOCIDADE_CORVO
        corvo["y"] += direcao.y * VELOCIDADE_CORVO

    else:
        corvo["x"] = corvo["alvo_x"]
        corvo["y"] = corvo["alvo_y"]

        
        if corvo["estado"] == "caçando":
            terreno = corvo["terreno_alvo"]

            if (terreno["planta"] is not None and terreno["planta"]["estado"] == "pronta"):
                corvo["estado"] = "comendo"
                corvo["tempo_comecou_comer"] = pygame.time.get_ticks()

            else:
                corvo["estado"] = "vigiando"
                corvo.pop("terreno_alvo", None)


def desenhar_corvo(tela, corvo):
    corvo_rect = pygame.Rect(int(corvo["x"]), int(corvo["y"]), TAMANHO_CORVO, TAMANHO_CORVO)

    pygame.draw.rect(tela, COR_CORVO, corvo_rect)

    
    bico = [(corvo_rect.right, corvo_rect.centery - 5), (corvo_rect.right + 10, corvo_rect.centery), (corvo_rect.right, corvo_rect.centery + 5)]

    pygame.draw.polygon(tela, (255, 200, 0), bico)