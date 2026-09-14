class GestorPersonas:
    def __init__(self):
        self.personas = {}

    def agregar_persona(self, nombre, edad):
        self.personas[nombre] = edad

    def personas_mayores(self, edad_minima):
        resultado = []

        for nombre, edad in self.personas.items():
            if edad >= edad_minima:
                resultado.append(nombre)

        return resultado

    def edad_promedio(self):
        return sum(self.personas.values()) / len(self.personas)


gp = GestorPersonas()

gp.agregar_persona("Emanuella", 18)
gp.agregar_persona("Roosevelt", 21)
gp.agregar_persona("Paula",19)
gp.agregar_persona("Amanda",20)
print(gp.personas_mayores(18))
print(gp.edad_promedio())