class AgrupadorEdades:

    def __init__(self):
        self.grupos = {}

    def clasificar_edad(self, edad):
        if edad <= 12:
            return "niño"
        elif edad <= 17:
            return "adolescente"
        elif edad <= 64:
            return "adulto"
        else:
            return "mayor"

    def agrupar_por_categoria(self, *edades):
        self.grupos = {}

        for edad in edades:
            categoria = self.clasificar_edad(edad)

            if categoria not in self.grupos:
                self.grupos[categoria] = []

            self.grupos[categoria].append(edad)

        return self.grupos

    def edad_promedio_categoria(self, categoria):
        edades = self.grupos[categoria]
        return sum(edades) / len(edades)


ae = AgrupadorEdades()

print(ae.agrupar_por_categoria(8, 1, 50, 155))

print(ae.edad_promedio_categoria("adulto"))
            


    
