class PlanificadorBrasil:
    def __init__(self):
        self.destinos = []

    def agregar_destinos(self, *destinos):
        for destino in destinos:
            self.destinos.append(destino)

    def presupuesto_total(self):
        total = 0

        for destino in self.destinos:
            ciudad, dias, presupuesto = destino
            total += presupuesto

        return total

    def ciudades_visitadas(self):
        ciudades = set()

        for destino in self.destinos:
            ciudad, dias, presupuesto = destino
            ciudades.add(ciudad)

        return ciudades

    def destino_mas_caro(self):
        mayor = self.destinos[0]

        for destino in self.destinos:
            if destino[2] > mayor[2]:
                mayor = destino
        return mayor
    def resumen(self):
        cantidad_ciudades = len(self.ciudades_visitadas())
        dias_totales = 0
        for destino in self.destinos:
            ciudad, dias, presupuesto = destino
            dias_totales += dias
        presupuesto = self.presupuesto_total()
        return (cantidad_ciudades, dias_totales, presupuesto)
planificador = PlanificadorBrasil()
planificador.agregar_destinos(
    ("Juazeiro", 5, 450),
    ("Salvador", 4, 380),
    ("Recife", 6, 520),
    ("Fortaleza", 3, 300),
    ("Sao Paulo", 5, 700),
    ("Juazeiro", 2, 180)
)
print("Destinos:", planificador.destinos)
print("Presupuesto total:", planificador.presupuesto_total())
print("Ciudades visitadas:", planificador.ciudades_visitadas())
print("Destino más caro:", planificador.destino_mas_caro())
print("Resumen:", planificador.resumen())