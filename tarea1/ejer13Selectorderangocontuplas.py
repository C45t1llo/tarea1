class SelectorRango:

    def crear_rango(self, inicio, fin):
        return tuple(range(inicio, fin))

    def elementos_en_multiples_rangos(self, *rangos):
        elementos = set()

        for rango in rangos:
            inicio, fin = rango

            for numero in range(inicio, fin):
                elementos.add(numero)

        return list(elementos)


selector = SelectorRango()

resultado1 = selector.crear_rango(1, 6)
print("Rango creado:", resultado1)
resultado2 = selector.elementos_en_multiples_rangos(
    (1, 5),
    (3, 8),
    (7, 10)
)

print("Elementos sin duplicados:", resultado2)