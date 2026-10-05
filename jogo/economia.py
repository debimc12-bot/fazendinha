from configuracao.configuracao import Configuracao

config = Configuracao()


def criar_economia():
    return {
        "moedas": config.moedas_iniciais,
        "diamantes": config.diamantes_iniciais
    }


def adicionar_moedas(economia, quantidade):
    economia["moedas"] += quantidade


def remover_moedas(economia, quantidade):
    if economia["moedas"] >= quantidade:
        economia["moedas"] -= quantidade
        return True

    return False


def adicionar_diamantes(economia, quantidade):
    economia["diamantes"] += quantidade


def remover_diamantes(economia, quantidade):
    if economia["diamantes"] >= quantidade:
        economia["diamantes"] -= quantidade
        return True

    return False