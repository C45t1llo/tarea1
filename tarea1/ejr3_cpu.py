class Analizadortexto:

    def __init__(self):
        self.palabra = set()
        self.orden = []

    def agregar_palabra(self, palabra):
        if palabra not in self.palabra:
            self.palabra.add(palabra)
            self.orden.append(palabra)

    def contar_palabra(self):
        return len(self.palabra)

    def agregar_multiples(self, *args):
        for palabra in args:
            self.agregar_palabra(palabra)


at = Analizadortexto()

at.agregar_multiples("Emanuella", "te amo", "hola", "brasil")

print(at.contar_palabra())