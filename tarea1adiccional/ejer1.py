class DetectorConsecutivos:
    def __init__(self):
        self.numeros = []

    def analizar(self, *numeros):
        self.numeros = list(numeros)


    def pares_consecutivos(self):
        lista = []
        for i in range(len(self.numeros)-1):
            if self.numeros[i + 1] == self.numeros[i] + 1:
                lista.append((self.numeros[i], self.numeros[i + 1]))
        return lista

    def cantidad_pares(self):
        return len(self.pares_consecutivos())


detector = DetectorConsecutivos()
detector.analizar(1, 2, 5, 6, 9, 10, 15, 16, 20, 21)
detector.cantidad_pares  ()
print(detector.pares_consecutivos())
print(detector.cantidad_pares())

                
    

              
                








