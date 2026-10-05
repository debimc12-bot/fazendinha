from configuracao.configuracao import Configuracao
from jogo.terreno import desenhar_terrenos
from jogo.plantas import desenhar_planta
from jogo.jogador import desenhar_jogador
from jogo.corvo import desenhar_corvo
from jogo.mala import desenhar_mala, desenhar_isca

config = Configuracao()

def desenhar_jogo(tela, terrenos, jogador, corvo, mala, fonte, plantas_colhidas, vidas):
    tela.fill(config.verde_grama)

    texto_colheita = fonte.render(f"Plantas colhidas: {plantas_colhidas}",True, config.cor_texto)
    tela.blit(texto_colheita, (20, 20))

    texto_vidas = fonte.render(f"Vidas: {vidas}", True, config.cor_texto)
    tela.blit(texto_vidas, (20, 55))

    desenhar_terrenos(tela, terrenos)

    for terreno in terrenos:
        desenhar_planta(tela, terreno["planta"], terreno)

    desenhar_jogador(tela, jogador)
    desenhar_corvo(tela, corvo)
    desenhar_mala(tela, mala)
    desenhar_isca(tela, mala)

def desenhar_pausa(tela, fonte, plantas_colhidas, plantas_comidas_corvo, vidas, economia, energia):
    tela.fill(config.preto)

    titulo = fonte.render("PAUSA", True, config.branco)

    tela.blit(titulo,(config.largura_tela // 2 - titulo.get_width() // 2, 50))

    informacoes = [
        f"Moedas: {economia['moedas']}",
        f"Diamantes: {economia['diamantes']}",
        f"Plantas colhidas: {plantas_colhidas}",
        f"Plantas comidas pelo corvo: {plantas_comidas_corvo}",
        f"Vidas: {vidas}",
        f"Energia: {energia['energia']}"
        ]

    y = 130

    for texto in informacoes:
        texto_renderizado = fonte.render(texto, True, config.cor_texto)
        tela.blit(texto_renderizado,(config.largura_tela // 2 - texto_renderizado.get_width() // 2, y))
        
        y += 45

    voltar = fonte.render("ESC - Voltar ao jogo", True, config.branco)
    tela.blit(voltar, (config.largura_tela // 2 - voltar.get_width() // 2, 500))