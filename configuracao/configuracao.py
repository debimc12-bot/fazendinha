from dataclasses import dataclass

@dataclass
class Configuracao:
    largura_tela: int = 800
    altura_tela: int = 600
    fps: int = 60
    titulo_jogo: str = "Minha Fazenda"

    verde_grama: tuple = (90, 180, 80)
    marrom_terra: tuple = (150, 100, 50)
    branco: tuple = (255, 255, 255)
    preto: tuple = (0, 0, 0)

    verde_semente: tuple = (80, 150, 80)
    verde_planta: tuple = (30, 140, 30)
    verde_pronta: tuple = (20, 100, 20)
    tempo_crescimento: int = 10

    tamanho_corvo: int = 30
    velocidade_corvo: int = 2
    cor_corvo: tuple = (25, 25, 25)
    cor_bico_corvo: tuple = (255, 200, 0)
    tempo_comendo: int = 1000

    mala_largura: int = 65
    mala_altura: int = 50
    mala_distancia_direita: int = 90
    mala_distancia_baixo: int = 75

    distancia_interacao_mala: int = 50
    cor_mala: tuple = (130, 75, 35)
    cor_tampa_mala: tuple = (90, 50, 25)
    cor_alca_mala: tuple = (60, 40, 25)

    cor_isca: tuple = (230, 190, 40)
    tamanho_isca: int = 7

    cor_texto: tuple = (255, 255, 255)
    tamanho_fonte_mala: int = 22

    cor_energia: tuple = (255, 220, 40)
    cor_fundo_energia: tuple = (70, 70, 70)

    tamanho_jogador: int = 30
    velocidade_jogador: int = 4

    tamanho_terreno: int = 50
    terreno_x: int = 100
    terreno_y: int = 100

    quantidade_colunas: int = 6
    quantidade_linhas: int = 4

    distancia_interacao: int = 40

    cor_borda_terra: tuple = (80, 50, 25)

    energia_maxima: int = 1000
    energia_inicial: int = 1000

    tempo_recuperacao_segundos: int = 3 * 60 * 60

    custo_preparar_terra: int = 10
    custo_plantar_semente: int = 5
    custo_regar_planta: int = 2
    custo_colher_planta: int = 5

    moedas_iniciais: int = 0
    diamantes_iniciais: int = 0

    MENU = "menu"
    JOGANDO = "jogando"
    PAUSADO = "pausado"
    FIM_DE_JOGO = "fim_de_jogo"




