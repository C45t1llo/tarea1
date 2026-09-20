class AnalizadorPatrones:
    def __init__(self):
        self.palabras = set()

    def encontrar_palabras(self, texto, patron):
        resultado = []
        palabras = texto.split()

        for palabra in palabras:
            self.palabras.add(palabra)

            if palabra.startswith(patron):
                resultado.append(palabra)

        return resultado

    def agrupar_por_longitud(self, texto):
        grupos = {}
        palabras = texto.split()

        for palabra in palabras:
            self.palabras.add(palabra)

            longitud = len(palabra)

            if longitud not in grupos:
                grupos[longitud] = []

            grupos[longitud].append(palabra)

        return grupos

    def palabras_unicas(self):
        return self.palabras


texto = "Emanuella te amo sé que hay mil razones para no estar juntos a veces tengo que dejarte ir para que tú estés feliz"

analizador = AnalizadorPatrones()

print("Palabras que empiezan con 'E':")
print(analizador.encontrar_palabras(texto, "E"))

print("\nPalabras agrupadas por longitud:")
print(analizador.agrupar_por_longitud(texto))

print("\nPalabras únicas:")
print(analizador.palabras_unicas())