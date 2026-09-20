class RegistroCiudades:
    def __init__(self):
        self.ciudades = []

    def registrar(self, *ciudades):
        for ciudad in ciudades:
            self.ciudades.append(ciudad)

    def agrupar_por_inicial(self):
        agrupadas = {}

        for ciudad in self.ciudades:
            inicial = ciudad[0].upper()

            if inicial not in agrupadas:
                agrupadas[inicial] = []

            agrupadas[inicial].append(ciudad)

        return agrupadas

    def ciudades_repetidas(self):
        repetidas = []

        for ciudad in self.ciudades:
            if self.ciudades.count(ciudad) > 1 and ciudad not in repetidas:
                repetidas.append(ciudad)

        return repetidas


# Prueba
registro = RegistroCiudades()

registro.registrar(
    "Juazeiro",
    "Salvador",
    "Recife",
    "Guayaquil",
    "Quito",
    "Cuenca",
    "Bogotá",
    "Medellín",
    "Cali",
    "Roma",
    "Milán",
    "Venecia",
    "Ciudad de México",
    "Cancún",
    "Guadalajara",
    "Juazeiro",
    "Quito"
)

print("Ciudades registradas:", registro.ciudades)
print("Agrupadas por inicial:", registro.agrupar_por_inicial())
print("Ciudades repetidas:", registro.ciudades_repetidas())