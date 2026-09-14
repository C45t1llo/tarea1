class ContadorFrecuencia:
    def __init__(self):
        self.repeticiones = {}

    def agregar_elemento(self, elemento):
        if elemento in self.repeticiones:
            self.repeticiones[elemento] = self.repeticiones[elemento] + 1
        else:
            self.repeticiones[elemento]= 1
            def elemento_mas_frecuencia(self):
                elemeneto_mayor = None
                frecuencia_mayor=0
                for elemento in self.repeticiones:
                    if self.repeticiones[elemento] > frecuencia_mayor:
                        frecuencia_mayor = self.repeticiones[elemento]
                        elemeneto_mayor = elemento

                        return elemeneto_mayor
                    def frecuencia_elemento(self,elemento):
                        if elemento in self.repeticiones:
                            return self.repeticiones[elemento]
                        else:
                            return 0
cf = ContadorFrecuencia()

cf.agregar_elemento("v")
cf.agregar_elemento("b")
cf.agregar_elemento("v")

print(cf.repeticiones)
print(cf.elemento_mas_frecuente())
print(cf.frecuencia_elemento("v")) 
                        
                    


            
        



            


 

