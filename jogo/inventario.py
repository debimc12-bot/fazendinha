def criar_inventario():
    return {
        "sementes": 0,
        "iscas": 0
    }


def adicionar_item(inventario, item, quantidade=1):
    if item not in inventario:
        inventario[item] = 0

    inventario[item] += quantidade


def remover_item(inventario, item, quantidade=1):
    if item not in inventario:
        return False

    if inventario[item] < quantidade:
        return False

    inventario[item] -= quantidade
    return True


def tem_item(inventario, item, quantidade=1):
    return inventario.get(item, 0) >= quantidade