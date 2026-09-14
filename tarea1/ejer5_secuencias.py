class InversonSecuencia:

    def __init__(self):
        pass

    def invertir_lista(self, lista):
        resultado = []

        for i in range(len(lista) - 1, -1, -1):
            resultado.append(lista[i])

        return resultado

    def invertir_multiples(self, *listas):
        resultado = {}

        for lista in listas:
            invertida = self.invertir_lista(lista)
            resultado[tuple(lista)] = invertida

        return resultado


inv = InversonSecuencia()

print(inv.invertir_multiples(
    [4, 5, 7],
    [8, 2, 1]
))



    


