class GestorTemperatura:
    def __init__(self):
        self.temperaturas = []

    def registrar_temperatura(self, temp):
        self.temperaturas.append(temp)

    def minima(self):
        return min(self.temperaturas)

    def maxima(self):
        return max(self.temperaturas)

    def promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

    def registrar_multiples(self, *temps):
        for temp in temps:
            self.registrar_temperatura(temp)


gt = GestorTemperatura()

gt.registrar_multiples(53, 15, 1, 3)

print("Mínima:", gt.minima())
print("Máxima:", gt.maxima())
print("Promedio:", gt.promedio())