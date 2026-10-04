import pygame
from configuracao.configuracao import Configuracao

config = Configuracao()

def criar_mala():
    return {
        "rect": pygame.Rect(config.largura_tela - config.mala_distancia_direita, config.altura_tela - config.mala_distancia_baixo, config.mala_largura, config.mala_altura),
        "isca_disponivel": True,
        "isca_no_chao": False,
        "isca_x": 0,
        "isca_y": 0
    }


def jogador_perto_da_mala(mala, jogador):
    jogador_rect = pygame.Rect(jogador["x"], jogador["y"], config.tamanho_jogador, config.tamanho_jogador)
    area_interacao = mala["rect"].inflate(config.distancia_interacao_mala, config.distancia_interacao_mala)

    return area_interacao.colliderect(jogador_rect)


def pegar_isca(mala, jogador):
    if not jogador_perto_da_mala(mala, jogador):
        return False

    if not mala["isca_disponivel"]:
        return False

    if jogador["tem_isca"]:
        return False

    jogador["tem_isca"] = True
    mala["isca_disponivel"] = False
    return True

def jogar_isca(mala, jogador):
    if not jogador["tem_isca"]:
        return False
    mala["isca_x"] = jogador["x"] + 15
    mala["isca_y"] = jogador["y"] + 15
    mala["isca_no_chao"] = True
    jogador["tem_isca"] = False

    return True

def desenhar_isca(tela, mala):
    if mala.get("isca_no_chao", False):
        pygame.draw.circle(tela, config.cor_isca, (int(mala["isca_x"]), int(mala["isca_y"])), config.tamanho_isca)


def desenhar_mala(tela, mala):
    rect = mala["rect"]

    pygame.draw.rect(tela, config.cor_mala, rect, border_radius = 5)
    pygame.draw.rect(tela, config.cor_tampa_mala, (rect.x, rect.y, rect.width, 12))
    pygame.draw.rect(tela, config.cor_alca_mala, (rect.centerx - 10, rect.y - 8, 20, 10), 3, border_radius = 3)

    
    fonte = pygame.font.Font(None, config.tamanho_fonte_mala)
    if mala["isca_disponivel"]:
        texto = fonte.render("E: pegar isca", True, config.cor_texto)
    else:
        texto = fonte.render("Sem isca", True, config.cor_texto)

    tela.blit(texto, (rect.x - 20, rect.y - 28))