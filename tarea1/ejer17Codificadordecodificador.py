class CodificadorCesar:
    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        numero = ord(letra)
        posicion = numero - 65
    
        nueva_posicion = (posicion + desplazamiento) % 26

        nueva_letra = chr(nueva_posicion + 65)

        return nueva_letra
    
    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""

        for letra in palabra:

            letra_codificada = self.codificar_letra(letra,desplazamiento)
            resultado += letra_codificada
        self.historial [palabra] = resultado
        return resultado
cesar = CodificadorCesar()

print(cesar.codificar_palabra("EMANUELLA", 3))
    




    





        
    



