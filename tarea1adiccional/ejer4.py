class OrganizadorColores:
    def __init__(self):
        self.colores = []
    def registrar(self,*colores):
            for color in colores:
             self.colores.append(color)
    def contar_colores(self):
                 conteo = {}
                 for color in self.colores:
                       if color in  conteo:
                             conteo[color ]+=1
                       else:
                             conteo[color]=1
                 return conteo
    def colores_unicos(self):
          unicos = set()
          for color in self.colores:
                unicos.add(color)
          return unicos
    def color_mas_repetido(self):
                conteo = self.contar_colores()
                mayor = 0
                color_mayor = None
                for color in conteo:
                       if conteo[color] > mayor:
                              mayor  = conteo[color]
                              color_mayor = color 
                return color_mayor
organizador = OrganizadorColores()
organizador.registrar("rojo", "azul", "rojo", "verde", "azul", "rojo")
print(organizador.contar_colores())
print(organizador.colores_unicos())
print(organizador.color_mas_repetido())
    
                       

              

                
                


                             
                       




