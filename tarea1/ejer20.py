class AnalizadorPatrones:

    def __init__(self):
        self.palabras = []

    def encontrar_palabras(self, texto, patron):

        palabras = texto.split()

        resultado = []

        for palabra in palabras:

            if palabra.startswith(patron):
                resultado.append(palabra)

        return resultado

    def agrupar_por_longitud(self, texto):

        self.palabras = texto.split()

        resultado = {}

        for palabra in self.palabras:

            longitud = len(palabra)

            if longitud not in resultado:
                resultado[longitud] = []

            resultado[longitud].append(palabra)

        return resultado

    def palabras_unicas(self):

        return set(self.palabras)


# Prueba
ap = AnalizadorPatrones()

print(ap.encontrar_palabras("Emanuella es increíble", "Ema"))

print(ap.agrupar_por_longitud("Emanuella es increíble"))

print(ap.palabras_unicas())

print("TE AMO EMANUELLA, NOS VEMOS 2029, BRASIL ")


