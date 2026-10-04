import pygame

from configuracao.configuracao import Configuracao

config = Configuracao()


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

        if tempo_atual - corvo["tempo_comecou_comer"] >= config.tempo_comendo:
            terreno = corvo["terreno_alvo"]
            terreno["planta"] = None

            corvo["estado"] = "vigiando"
            corvo.pop("terreno_alvo")

            return True

        return False

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
            corvo["x"] += (dx / distancia) * config.velocidade_corvo
            corvo["y"] += (dy / distancia) * config.velocidade_corvo

        return False

    plantas_maduras = [
        terreno
        for terreno in terrenos
        if terreno["planta"] is not None
        and terreno["planta"]["estado"] == "pronta"
    ]

    if plantas_maduras:
        terreno_alvo = min(
            plantas_maduras,
            key=lambda terreno: pygame.Vector2(corvo["x"] + config.tamanho_corvo / 2, corvo["y"] + config.tamanho_corvo / 2).distance_to(terreno["rect"].center))

        corvo["estado"] = "caçando"
        corvo["terreno_alvo"] = terreno_alvo
        corvo["alvo_x"] = (terreno_alvo["rect"].centerx - config.tamanho_corvo / 2)
        corvo["alvo_y"] = (terreno_alvo["rect"].centery - config.tamanho_corvo / 2)

    else:
        corvo["estado"] = "vigiando"
        return False

    diferenca_x = corvo["alvo_x"] - corvo["x"]
    diferenca_y = corvo["alvo_y"] - corvo["y"]

    distancia = pygame.Vector2(diferenca_x, diferenca_y).length()

    if distancia > config.velocidade_corvo:
        direcao = pygame.Vector2(diferenca_x, diferenca_y).normalize()

        corvo["x"] += direcao.x * config.velocidade_corvo
        corvo["y"] += direcao.y * config.velocidade_corvo

    else:
        corvo["x"] = corvo["alvo_x"]
        corvo["y"] = corvo["alvo_y"]

        if corvo["estado"] == "caçando":
            terreno = corvo["terreno_alvo"]

            if (terreno["planta"] is not None
                and terreno["planta"]["estado"] == "pronta"):
                corvo["estado"] = "comendo"
                corvo["tempo_comecou_comer"] = pygame.time.get_ticks()

            else:
                corvo["estado"] = "vigiando"
                corvo.pop("terreno_alvo", None)

    return False


def desenhar_corvo(tela, corvo):
    corvo_rect = pygame.Rect(
        int(corvo["x"]),
        int(corvo["y"]),
        config.tamanho_corvo,
        config.tamanho_corvo)

    pygame.draw.rect(tela,config.cor_corvo,corvo_rect)

    bico = [(corvo_rect.right,corvo_rect.centery - 5),(corvo_rect.right + 10, corvo_rect.centery),(corvo_rect.right,corvo_rect.centery + 5)]

    pygame.draw.polygon(tela, config.cor_bico_corvo, bico)
