class Inventario:
    def __init__(self):
        self.productos = {}

    def agregar_stock(self, producto, cantidad):
        if producto in self.productos:
            self.productos[producto] += cantidad
        else:
            self.productos[producto] = cantidad

    def restar_stock(self, restar, cantidad):
        if self.productos[restar] >= cantidad:
            self.productos[restar] -= cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        lista = []

        for productos in self.productos:
            if self.productos[productos] < minimo:
                lista.append(productos)

        return lista


inventario = Inventario()

inventario.agregar_stock("Volkswagen Gol", 10)
inventario.agregar_stock("Fiat Argo", 4)
inventario.agregar_stock("Chevrolet Onix", 2)

print("Inventario de carros:", inventario.productos)

print("¿Se pudo restar?:", inventario.restar_stock("Volkswagen Gol", 3))

print("Inventario después de la venta:", inventario.productos)

print("Carros con bajo stock:", inventario.productos_bajo_stock(5))








