class Inventario:

    def __init__(self):
        self.stock = {}

    def agregar_stock(self, producto, cantidad):
        self.stock[producto] = cantidad

    def restar_stock(self, producto, cantidad):
        if self.stock[producto] >= cantidad:
            self.stock[producto] = self.stock[producto] - cantidad
            return True
        return False

    def productos_bajo_stock(self, minimo):
        productos = []

        for producto, cantidad in self.stock.items():
            if cantidad < minimo:
                productos.append(producto)

        return productos


inv = Inventario()

inv.agregar_stock("arroz", 80)

print(inv.restar_stock("pan", 30))

print(inv.productos_bajo_stock(25))






            

        
    
        
        