from jogo.economia import remover_moedas


def criar_loja():
    return {
        "sementes": {
            "preco": 5,
            "quantidade": 1
        },
        "isca": {
            "preco": 10,
            "quantidade": 1
        }
    }


def comprar_item(loja, economia, item):
    if item not in loja:
        return False

    preco = loja[item]["preco"]

    if remover_moedas(economia, preco):
        return True

    return False