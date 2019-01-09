class SuperHeroe:
    def __init__(self, nombre, nacionalidad, estatura, peso, poderes=None, apodo=None):
        if poderes is None:
            poderes = []
        if apodo is None:
            apodo = {nombre}
        self.nombre = nombre
        self.apodos = apodo
        if self.apodos is None:
            self.apodos = nombre

        self.nacionalidad = nacionalidad
        self.estatura = estatura
        self.peso = peso
        self.poderes = poderes

    def añadir_apodo(self, apodo):
        self.apodos.append(apodo)

    def eliminar_apodo(self, apodo):
        self.apodos.remove(apodo)
        if self.apodos.isempty():
            self.apodos.append(self.nombre)

    def retirarse(self):
        self.apodos = set()

    def __str__(self):
        return self.nombre + ","


def guardar_a_fichero(list):
    with open("superheroes.txt", mode="w") as f:
        for e in list:
            print(e)


superheroes = []
superheroes.append(SuperHeroe("Superman", "España", estatura=180, peso=80.0, poderes=["volar"]))
guardar_a_fichero(superheroes)
