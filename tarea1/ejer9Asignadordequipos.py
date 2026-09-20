class Equipos:

    def __init__(self):
        self.equipos = {}

    def crear_equipo(self, nombre_equipo):
        self.equipos[nombre_equipo] = []

    def agregar_jugador(self, equipo, jugador):
        self.equipos[equipo].append(jugador)

    def equipo_mayor_integrantes(self):
        mayor = None

        for equipo, jugadores in self.equipos.items():
            if mayor is None or len(jugadores) > len(self.equipos[mayor]):
                mayor = equipo

        return mayor


equipos = Equipos()

equipos.crear_equipo("Arsenal")
equipos.crear_equipo("PSG")
equipos.crear_equipo("Real Madrid")


equipos.agregar_jugador("Arsenal", "Kai Havertz")
equipos.agregar_jugador("Arsenal", "Bukayo Saka")
equipos.agregar_jugador("Arsenal", "Piero Hincapie")


equipos.agregar_jugador("PSG", "Ousmane Dembele")
equipos.agregar_jugador("PSG", "Khvicha Kvaratskhelia")
equipos.agregar_jugador("PSG", "Vitinha")
equipos.agregar_jugador("PSG", "Achraf Hakimi")


equipos.agregar_jugador("Real Madrid", "Kylian Mbappe")
equipos.agregar_jugador("Real Madrid", "Vinicius Junior")


print("Equipos:", equipos.equipos)

print("Equipo con más integrantes:",
      equipos.equipo_mayor_integrantes())





        