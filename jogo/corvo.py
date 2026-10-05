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
        "tempo_comecou_comer": 0,
        "tempo_comecou_ataque": 0,
        "tempo_ultimo_ataque": 0
    }


def atualizar_comida(corvo):
    tempo_atual = pygame.time.get_ticks()

    if tempo_atual - corvo["tempo_comecou_comer"] >= config.tempo_comendo:
        terreno = corvo["terreno_alvo"]
        terreno["planta"] = None

        corvo["estado"] = "vigiando"
        corvo.pop("terreno_alvo")

        return "planta_comida"

    return None

def mover_para_isca(corvo, mala):
    alvo_x = mala["isca_x"]
    alvo_y = mala["isca_y"]

    dx = alvo_x - (corvo["x"] + 15)
    dy = alvo_y - (corvo["y"] + 15)

    distancia = (dx ** 2 + dy ** 2) ** 0.5

    if distancia <= 5:
        mala["isca_no_chao"] = False
        corvo["estado"] = "parado"
        return

    corvo["x"] += (dx / distancia) * config.velocidade_corvo
    corvo["y"] += (dy / distancia) * config.velocidade_corvo

def encontrar_planta_pronta(corvo, terrenos):
    plantas_pronta = [
        terreno for terreno in terrenos if terreno["planta"]
        is not None and terreno["planta"]["estado"] == "pronta"
        ]

    if not plantas_pronta:
        return None

    return min(plantas_pronta, key=lambda terreno: pygame.Vector2(
        corvo["x"] + config.tamanho_corvo / 2,
        corvo["y"] + config.tamanho_corvo / 2
    ).distance_to(terreno["rect"].center))

def definir_alvo(corvo, terrenos):
    terreno_alvo = encontrar_planta_pronta(corvo, terrenos)

    if terreno_alvo is not None:
        corvo["estado"] = "cacando"
        corvo["terreno_alvo"] = terreno_alvo

        corvo["alvo_x"] = (terreno_alvo["rect"].centerx - config.tamanho_corvo / 2)    
        corvo["alvo_y"] = (terreno_alvo["rect"].centery - config.tamanho_corvo / 2)

def mover_para_alvo(corvo):
    diferenca_x = corvo["alvo_x"] - corvo["x"]
    diferenca_y = corvo["alvo_y"] - corvo["y"]

    distancia = pygame.Vector2(diferenca_x, diferenca_y).length()

    if distancia <= config.velocidade_corvo:
        corvo["x"] = corvo["alvo_x"]
        corvo["y"] = corvo["alvo_y"]
        return True

    direcao = pygame.Vector2(diferenca_x, diferenca_y).normalize()

    corvo["x"] += direcao.x * config.velocidade_corvo
    corvo["y"] += direcao.y * config.velocidade_corvo

    return False

def atacar_jogador(corvo, jogador):
    tempo_atual = pygame.time.get_ticks()

    tempo_ataque = (tempo_atual - corvo["tempo_comecou_ataque"]) / 1000

    if tempo_ataque >= config.tempo_ataque_corvo:
        corvo["estado"] = "vigiando"
        return None

    velocidade = config.velocidade_ataque_corvo

    dx = jogador["x"] - corvo["x"]
    dy = jogador["y"] - corvo["y"]

    distancia = (dx ** 2 + dy ** 2) ** 0.5

    if distancia > 0:
        corvo["x"] += (dx / distancia) * velocidade
        corvo["y"] += (dy / distancia) * velocidade

    corvo_rect = pygame.Rect(int(corvo["x"]),
                             int(corvo["y"]),
                             config.tamanho_corvo,
                             config.tamanho_corvo)

    jogador_rect = pygame.Rect(jogador["x"],
                               jogador["y"],
                               config.tamanho_jogador,
                               config.tamanho_jogador)

    if corvo_rect.colliderect(jogador_rect):
        tempo_desde_ultimo_ataque = (
            tempo_atual - corvo["tempo_ultimo_ataque"]
        ) / 1000

        if (tempo_desde_ultimo_ataque >= config.tempo_entre_ataques_corvo):
            corvo["tempo_ultimo_ataque"] = tempo_atual
            return "atacou_jogador"
        
    return None

def verificar_chegada(corvo):
    if corvo["estado"] == "cacando":
        terreno = corvo["terreno_alvo"]

        if(terreno["planta"] is not None
           and terreno["planta"]["estado"] == "pronta"):

            corvo["estado"] = "comendo"
            corvo["tempo_comecou_comer"] = pygame.time.get_ticks()

        else:
            corvo["estado"] = "atacando"
            corvo["tempo_comecou_ataque"] = pygame.time.get_ticks()

            corvo.pop("terreno_alvo", None)

    return None

def mover_corvo(corvo, terrenos, mala, jogador):
    if corvo["estado"] == "atacando":
        return atacar_jogador(corvo, jogador)

    if corvo["estado"] == "comendo":
        return atualizar_comida(corvo)

    if mala["isca_no_chao"]:
        mover_para_isca(corvo, mala)
        return None

    if corvo["estado"] == "parado":
        corvo["estado"] = "vigiando"

    if corvo["estado"] == "vigiando":
        definir_alvo(corvo, terrenos)

    if corvo["estado"] == "cacando":
        chegou = mover_para_alvo(corvo)

        if chegou:
            return verificar_chegada(corvo)

    return None

def desenhar_corvo(tela, corvo):
    corvo_rect = pygame.Rect(int(corvo["x"]),
                             int(corvo["y"]),
                             config.tamanho_corvo,
                             config.tamanho_corvo)

    pygame.draw.rect(tela, config.cor_corvo, corvo_rect)

    bico = [(corvo_rect.right, corvo_rect.centery - 5),
            (corvo_rect.right + 10, corvo_rect.centery),
            (corvo_rect.right, corvo_rect.centery + 5)]
    
    pygame.draw.polygon(tela, config.cor_bico_corvo, bico)
