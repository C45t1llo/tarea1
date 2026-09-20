class CalculadorViaje:
    def __init__(self):
        self.viajes = []

    def agregar_tramos(self, *tramos):
        for tramo in tramos:
            self.viajes.append(tramo)
    def tiempo_total(self):
        total = 0
        for tramo in self.viajes:
            total += tramo[2]
        return total
    def tramos_largos(self, limite):
        lista = []
        for tramo in self.viajes:
            if tramo[2] > limite:
                lista.append(tramo)
        return lista


viaje = CalculadorViaje()

viaje.agregar_tramos(
    ("Guayaquil", "São Paulo", 3600),
    ("São Paulo", "Juazeiro do Norte", 2100)
)
print("Tiempo total:", viaje.tiempo_total(), "minutos")
print("Tramos largos:", viaje.tramos_largos(2500))


