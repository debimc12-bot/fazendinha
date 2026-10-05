from configuracao.configuracao import Configuracao
from jogo.terreno import desenhar_terrenos
from jogo.plantas import desenhar_planta
from jogo.jogador import desenhar_jogador
from jogo.corvo import desenhar_corvo
from jogo.mala import desenhar_mala, desenhar_isca

config = Configuracao()

def desenhar_jogo(tela,terrenos,jogador,corvo,mala,fonte,plantas_colhidas,vidas):
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