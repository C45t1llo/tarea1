class CombinadorListas:

    def intercalar(self, lista1, lista2):
        resultado = []

        for i in range(len(lista1)):
            resultado.append(lista1[i])
            resultado.append(lista2[i])

        return resultado

    def intercalar_multiples(self, *listas):
        resultado = []

        for i in range(len(listas[0])):
            for lista in listas:
                resultado.append(lista[i])

        return resultado


cl = CombinadorListas()

print(cl.intercalar([9,3], [5, 6]))
print(cl.intercalar_multiples([6, 2], [4, 8], [22, 49]))