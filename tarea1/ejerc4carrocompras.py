class CarroCompras:

    def __init__(self):
        self.articulos = {}

    def agregar_articulo(self, nombre, precio):
        self.articulos[nombre] = precio

    def total_carrito(self):
        return sum(self.articulos.values())

    def articulos_por_rango(self, precio_min, precio_max):
        resultado = []

        for nombre, precio in self.articulos.items():
            if precio_min <= precio <= precio_max:
                resultado.append(nombre)

        return resultado


c = CarroCompras()

c.agregar_articulo("atun", 2.50)
c.agregar_articulo("monster", 3.00)
c.agregar_articulo("cocacola",1.25)
c.agregar_articulo("pizza",20.50)

print(c.total_carrito())
print(c.articulos_por_rango(2, 3))