def annadir(agn, nombre, tlf):
    agn[nombre] = agn.get(nombre, {tlf})
    return agn


def eliminar(agn, nombre, tlf):
    if nombre in agn:
        if tlf in agn[nombre]:
            agn[nombre] = agn.get(nombre, set()).remove(tlf)
            if agn[nombre] is None:
                agn.pop(nombre)
    return agn


def existe(agn, nombre, tlf):
    if nombre in agn:
        if tlf in agn[nombre]:
            return True
    return False


agenda = {}
agenda = annadir(agenda, 'Hugo', '1234')
print(agenda)
agenda = annadir(agenda, 'Ramon', '12345')
print(agenda)
agenda = annadir(agenda, 'pepe', '123456')
print(agenda)
agenda = eliminar(agenda, 'Ramon', '12345')
print(agenda)
print(existe(agenda, 'Hugo', '1234'))
print(existe(agenda, 'Ramon', '9876'))
