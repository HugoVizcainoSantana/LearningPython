import random


class Persona:
    def __init__(self, nombre, estatura, peso, nacionalidad):
        self.nombre = nombre
        self.estatura = estatura
        self.peso = peso
        self.nacionalidad = nacionalidad


class SuperPersona(Persona):
    def __init__(self, nombre, estatura, peso, nacionalidad, poderes=set(), apodos=set()):
        super(SuperPersona, self).__init__(nombre, estatura, peso, nacionalidad)
        self.poderes = poderes
        self.apodos = apodos

    def actuar(self, ciudad):
        self.__actuar__(ciudad, "esta")

    def __actuar__(self, ciudad, accion):
        """
        :param accion:
        :type ciudad: str
        """
        print(self.apodo_aleatorio() + " " + accion + " en la ciudad de " + ciudad)

    def apodo_aleatorio(self):
        return random.sample(self.apodos, 1)[0]

    def tener_hijo(self, progenitor):
        poderes_comunes = {}
        for pod in self.poderes:
            poderes_comunes[pod] = poderes_comunes.get(pod, 0) + 1

        for pod in progenitor.poderes:
            poderes_comunes[pod] = poderes_comunes.get(pod, 0) + 1

        print("Poderes comunes: " + str(poderes_comunes))
        poderes_hijo = set()
        for poder, veces in poderes_comunes.items():
            print("El Hijo tiene " + str(len(poderes_hijo)) + " poderes")
            print("Poder: " + str(poder))
            prob_base = 0.5 * veces
            prob_1 = random.random()
            print("\tProb Base:" + str(prob_base))
            print("\tProb 1:" + str(prob_1))
            if prob_1 <= prob_base:
                prob_segunda = prob_1 / max(len(poderes_hijo), 1)
                prob_2 = random.random()
                print("\tProb Segunda: " + str(prob_segunda))
                print("\tProb 2:" + str(prob_2))
                if prob_2 <= prob_1 / max(len(poderes_hijo), 1):
                    poderes_hijo.add(poder)

        return SuperPersona(
            "Hijo de " + self.nombre + " y " + progenitor.nombre,
            0.40,
            4.200,
            "España",
            poderes_hijo,
            set("SuperHijo")
        )


class SuperHeroe(SuperPersona):
    def __init__(self, nombre, estatura, peso, nacionalidad, poderes=set(), apodos=set()):
        super(SuperHeroe, self).__init__(nombre, estatura, peso, nacionalidad, poderes, apodos)

    def actuar(self, ciudad):
        super(SuperHeroe, self).__actuar__(ciudad, "salva")


class SuperVillano(SuperPersona):
    def __init__(self, nombre, estatura, peso, nacionalidad, poderes=set(), apodos=set()):
        super(SuperVillano, self).__init__(nombre, estatura, peso, nacionalidad, poderes, apodos)

    def actuar(self, ciudad):
        super(SuperVillano, self).__actuar__(ciudad, "ataca")


s1 = SuperHeroe("Super Man", 1.80, 85, "España", {"Volar", "SuperFuerza"}, {"El Super Hombre"})
s2 = SuperHeroe("Super Woman", 1.60, 75, "España", {"Volar", "Vision Laser", "Super oido"}, {"La Super Mujer"})
s1.actuar("Madrid")
s2.actuar("Valencia")
hijo = s1.tener_hijo(s2)
print("Super poderes de hijo")
for p in hijo.poderes:
    print(p)
