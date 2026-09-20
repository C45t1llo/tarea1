class AnalizadorTemperaturas:
    def __init__(self):
        self.temperaturas = []

    def registrar(self, *temperaturas):
        for temperatura in temperaturas:
            self.temperaturas.append(temperatura)

    def clasificar(self):
        categorias = {
            "baja": [],
            "normal": [],
            "alta": []
        }

        for temperatura in self.temperaturas:
            if temperatura < 15:
                categorias["baja"].append(temperatura)
            elif temperatura <= 30:
                categorias["normal"].append(temperatura)
            else:
                categorias["alta"].append(temperatura)

        return categorias

    def temperatura_extrema(self):
        menor = min(self.temperaturas)
        mayor = max(self.temperaturas)

        return (menor, mayor)

    def dias_calientes(self, limite):
        calientes = []

        for temperatura in self.temperaturas:
            if temperatura > limite:
                calientes.append(temperatura)

        return calientes
analizador = AnalizadorTemperaturas()

analizador.registrar(
    12, 18, 25, 32, 35,
    14, 28, 31, 22, 16
)
print("Temperaturas:", analizador.temperaturas)
print("Clasificación:", analizador.clasificar())
print("Temperatura extrema:", analizador.temperatura_extrema())
print("Días calientes:", analizador.dias_calientes(30))