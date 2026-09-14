class AnalizadorString:
    def __init__(self):
        self.texto_mas_largo = ""

    def solo_vocales(self, letra):
        return letra.lower() in "aeiou"

    def contar_por_tipo(self, texto):
        conteo = {
            "vocales": 0,
            "consonantes": 0,
            "digitos": 0
        }

        for letra in texto:
            if self.solo_vocales(letra):
                conteo["vocales"] += 1
            elif letra.isdigit():
                conteo["digitos"] += 1
            else:
                conteo["consonantes"] += 1

        if len(texto) > len(self.texto_mas_largo):
            self.texto_mas_largo = texto

        return conteo


astr = AnalizadorString()

print(astr.contar_por_tipo("Te amo Emanuella regresa 22"))