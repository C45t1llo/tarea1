class RegistroPeliculas:
    def __init__(self):
        self.peliculas = ()
    def agregar(self,*peliculas):
        for pelicula in peliculas:
         self.peliculas +=(pelicula,)

    def buscar_por_genero(self,genero):
            titulos = ()
            for pelicula in self.peliculas:
                if pelicula [1]== genero:
                    titulos +=(pelicula[0],)
            return titulos
    def mejor_puntuada(self):
        mejor = self.peliculas[0]
        for pelicula in self.peliculas:
            if pelicula[2] >mejor[2]:
                mejor = pelicula
        return mejor


registro = RegistroPeliculas()
registro.agregar(
    ("Steve Jobs", "Tecnología", 7.2),
    ("La red social", "Tecnología", 7.8),
    ("La teoría del todo", "Ciencia", 7.7),
    ("Interestelar", "Ciencia ficción", 8.7),
    ("2001: Una odisea del espacio", "Ciencia ficción", 8.3),
    ("Oppenheimer", "Ciencia", 8.6),
    ("The Imitation Game", "Tecnología", 8.0),
    ("Hidden Figures", "Ciencia", 7.8),
    ("Apollo 13", "Ciencia", 7.7)
)
print(registro.peliculas)
print(registro.buscar_por_genero("Ciencia"))
print(registro.mejor_puntuada())




               




