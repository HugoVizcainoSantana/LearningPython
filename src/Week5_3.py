import random
import statistics

propiedades_inmobiliarias = []
for i in range(100):
    propiedades_inmobiliarias.append((
        random.sample(["Casa", "Comercio", "Terreno Rustico"], 1)[0],
        random.randint(20000, 500000)
    ))

print(propiedades_inmobiliarias)
propiedades_precios = {}
for propiedad, precio in propiedades_inmobiliarias:
    aux = propiedades_precios.get(propiedad, [])
    aux.append(precio)
    propiedades_precios[propiedad] = aux

print("Medias")
for k, v in propiedades_precios.items():
    print("\t" + k)
    print(statistics.mean(v))
    print("")
