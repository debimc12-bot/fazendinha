import time

from configuracao.configuracao import Configuracao

config = Configuracao()


def criar_energia():
    return {
        "energia": config.energia_inicial,
        "ultima_recuperacao": time.time()
    }


def tem_energia(energia, quantidade):
    return energia["energia"] >= quantidade


def gastar_energia(energia, quantidade):
    if not tem_energia(energia, quantidade):
        return False

    energia["energia"] -= quantidade
    return True


def recuperar_energia(energia):
    tempo_atual = time.time()

    tempo_passado = (
        tempo_atual - energia["ultima_recuperacao"]
    )

    if tempo_passado >= config.tempo_recuperacao_segundos:
        energia["energia"] = config.energia_maxima
        energia["ultima_recuperacao"] = tempo_atual


def obter_energia(energia):
    return energia["energia"]