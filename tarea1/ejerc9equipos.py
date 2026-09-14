class Equipos:
    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        mayor = 0
        equipo_mayor = ""

        for equipo, jugadores in self.equipos.items():
            if len(jugadores) > mayor:
                mayor = len(jugadores)
                equipo_mayor = equipo

        return equipo_mayor


eq = Equipos()

eq.crear_equipo("A")
eq.crear_equipo("B")
eq.crear_equipo("C")

eq.agregar_jugador("A", "Andres")
eq.agregar_jugador("A", "Emanuella")

eq.agregar_jugador("B", "Paula")

eq.agregar_jugador("C", "Amanda")
eq.agregar_jugador("C", "Roosevelt")
eq.agregar_jugador("C", "Justo")

print(eq.equipo_mayor_integrantes())
