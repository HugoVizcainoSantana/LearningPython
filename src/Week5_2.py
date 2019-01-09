def recibir_numero():
    try:
        return int(input("Introduzca un numero:\n"))
    except ValueError:
        print("Error... no se ha introducido un numero")
        return recibir_numero()


# print(recibir_numero())


def dict_get(dictio: dict, key, default):
    try:
        return dictio[key]
    except KeyError:
        return default


print(dict_get({1: 2, 2: 3}, 3, 0))
