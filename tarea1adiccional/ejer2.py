class RegistroIdiomas:
    def __init__(self):
        self.personas = []
    def registrar(self,*personas):
        for persona in personas:
            self.personas.append(persona)
    def personas_por_idioma(self, idioma):
        lista = []
        for persona in self.personas:
            if persona [1] == idioma:
                lista.append(persona[0])
        return lista
    def idiomas_unicos(self):
        idiomas = set()
        for persona in self.personas:
            idiomas.add(persona[1])

        return idiomas 
registro = RegistroIdiomas()

registro.registrar(("Roosevelt", "Portugués"), ("Paula", "Inglés"), ("Emanuella", "Portugués"))

print(registro.personas_por_idioma("Portugués"))
print(registro.idiomas_unicos())

            





        
