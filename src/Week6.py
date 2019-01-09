import random
import statistics
from datetime import datetime


def fecha_aleatoria():
    day = random.randint(1, 365)
    return datetime.strptime("2018-" + str(day), "%Y-%j")


# noinspection NonAsciiCharacters
def paradoja_cumpleaños(debug=True):
    cumpleaños = set()
    f = None
    while True:
        f = fecha_aleatoria()
        if f in cumpleaños:
            break
        cumpleaños.add(f)
    if debug:
        print("Fecha que coincidio: " + str(f))
        print("Fechas necesarias: " + str(len(cumpleaños)))

    return len(cumpleaños) + 1


def comprobar_paradoja(n=10000):
    resultados = []
    for i in range(n):
        resultados.append(paradoja_cumpleaños(False))
        prct = i / n * 100
        if prct % random.uniform(1, 10) <= 0.25:
            print(str(prct) + "%")
    print("Resultados:")
    print(resultados)
    print("Media")
    print(statistics.mean(resultados))


def comprobar_con_tiempo():
    import time
    inicio = time.time()
    comprobar_paradoja()
    print("Tiempo (s):")
    print(time.time() - inicio)
