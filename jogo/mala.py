import pygame
from configuracao.configuracao import LARGURA_TELA, ALTURA_TELA

def criar_mala():
    return {
        "rect": pygame.Rect(LARGURA_TELA - 90, ALTURA_TELA - 75, 65, 50),
        "isca_disponivel": True,
        "isca_no_chao": False,
        "isca_x": 0,
        "isca_y": 0
    }


def jogador_perto_da_mala(mala, jogador):
    jogador_rect = pygame.Rect(jogador["x"], jogador["y"], 30, 30)
    area_interacao = mala["rect"].inflate(50, 50)

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
        pygame.draw.circle(tela, (230, 190, 40), (int(mala["isca_x"]), int(mala["isca_y"])), 7)


def desenhar_mala(tela, mala):
    rect = mala["rect"]

    pygame.draw.rect(tela, (130, 75, 35), rect, border_radius = 5)
    pygame.draw.rect(tela, (90, 50, 25), (rect.x, rect.y, rect.width, 12))
    pygame.draw.rect(tela, (60, 40, 25), (rect.centerx - 10, rect.y - 8, 20, 10), 3, border_radius = 3)

    
    fonte = pygame.font.Font(None, 22)
    if mala["isca_disponivel"]:
        texto = fonte.render("E: pegar isca", True, (255, 255, 255))
    else:
        texto = fonte.render("Sem isca", True, (255, 255, 255))

    tela.blit(texto, (rect.x - 20, rect.y - 28))