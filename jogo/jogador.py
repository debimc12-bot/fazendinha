import pygame

from configuracao.configuracao import Configuracao
config = Configuracao()

def criar_jogador():
    return {
        "x": config.largura_tela // 2,
        "y": config.altura_tela // 2
    }

def mover_jogador(jogador, teclas):
    if teclas[pygame.K_LEFT]:
        jogador["x"] -= config.velocidade_jogador

    if teclas[pygame.K_RIGHT]:
        jogador["x"] += config.velocidade_jogador

    if teclas[pygame.K_UP]:
        jogador["y"] -= config.velocidade_jogador

    if teclas[pygame.K_DOWN]:
        jogador["y"] += config.velocidade_jogador

   
    jogador["x"] = max(0, min(jogador["x"], config.largura_tela - config.tamanho_jogador))

    jogador["y"] = max(0, min(jogador["y"], config.altura_tela - config.tamanho_jogador))


def desenhar_jogador(tela, jogador):
    jogador_rect = pygame.Rect(jogador["x"], jogador["y"], config.tamanho_jogador, config.tamanho_jogador)

    pygame.draw.rect(tela, config.branco, jogador_rect)