class Controlgastos:
    def __init__(self):
        self.control = {}
    def registrar(self,gasto,cantidad):
        self.control[gasto] = cantidad
    def aumentar(self,gasto,cantidad):
        self.control[gasto] = self.control[gasto] + cantidad
    def total(self):
        total = 0
        for cantidad in self.control.values():
            total = total + cantidad
        return  total
    def gastos_mayores(self,limite):
        mayores = {}
        for gasto, cantidad in self.control.items():
            if cantidad > limite:
                mayores[gasto] = cantidad
        return mayores
control = Controlgastos()
control.registrar("Comida",45)
control.registrar("Transporte", 15)
control.registrar("Internet", 25)
print(control.control)
print(control.total())
print(control.gastos_mayores(20))
control.aumentar("Comida", 10)
print(control.control)








        
