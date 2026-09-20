class ControlEquipaje:
    def __init__(self):
        self.equipaje = []
    def registrar (self,*maletas):
        for maleta in maletas:
         self.equipaje.append(maleta)
    def equipaje_excedido(self, limite):
            peso = []
            for maleta in self.equipaje:
                persona,peso_maleta = maleta
                if peso_maleta > limite:
                    peso.append(persona)
            return peso
    def peso_total(self):
        total = 0
        for maleta in self.equipaje:
         persona,peso_maleta = maleta
         total +=peso_maleta
        return total
control = ControlEquipaje()

control.registrar(
    ("Emanuella", 18),
    ("Paula", 23),
    ("Jefferson", 15),
    ("Amanda", 30)
)

print("Equipaje:", control.equipaje)
print("Excedidos:", control.equipaje_excedido(20))
print("Peso total:", control.peso_total())


        




               
               




    # def registrar(self, *productos):
    #     for producto in productos:
    #         self.productos.append(producto)
    # def precio_promedio(self, categoria):
    #     precio = []
    #     for producto in self.productos:
    #         nombre, categoria_produ