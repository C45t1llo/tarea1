class CodificadorCesar:

    def __init__(self):
        self.historial = {}

    def codificar_letra(self, letra, desplazamiento):
        codigo = ord(letra)
        nuevo_codigo = (codigo - ord("a") + desplazamiento) % 26 + ord("a")
        return chr(nuevo_codigo)

    def codificar_palabra(self, palabra, desplazamiento):
        resultado = ""

        for letra in palabra:
            resultado += self.codificar_letra(letra, desplazamiento)

        self.historial[palabra] = resultado

        return resultado


cc = CodificadorCesar()

print(cc.codificar_letra("m", 3))
print(cc.codificar_palabra("emanuella", 3))
print(cc.historial)