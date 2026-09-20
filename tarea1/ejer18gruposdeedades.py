class AgrupadorEdades:

    def __init__(self):
        self.historial = {}

    def clasificar_edad(self, edad):
        if edad <= 11:
            return "niño"
        elif edad <= 17:
            return "adolescente"
        elif edad <= 64:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        categorias = {
            "niño": [],
            "adolescente": [],
            "adulto": [],
            "mayor": []
        }

        for edad in edades:
            categoria = self.clasificar_edad(edad)
            categorias[categoria].append(edad)
        self.historial = categorias

        return categorias

    def edad_promedio_categoria(self, categoria):
        edades = self.historial[categoria]
        suma = sum (edades)
        cantidad = len(edades)
        promedio = suma / cantidad
        return promedio




agrupador = AgrupadorEdades()

print(agrupador.agrupar_por_categoria(
    2, 5, 15, 13, 66, 18, 22, 66, 23, 55, 95
))

print(agrupador.edad_promedio_categoria("adulto"))