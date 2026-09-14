class AnalizadorNumeros:
    def __init__(self):
        self.pares = []
        self.impares = []

    def es_par(self, numero):
        return numero % 2 == 0

    def separar(self, *numeros):
        for numero in numeros:
            if self.es_par(numero):
                self.pares.append(numero)
            else:
                self.impares.append(numero)

        return {
            'pares': self.pares,
            'impares': self.impares
        }

    def cantidad_pares_impares(self):
        return len(self.pares), len(self.impares)


an = AnalizadorNumeros()

print(an.separar(2, 46, 7, 16, 7, 9, 1, 6))
print(an.cantidad_pares_impares())
