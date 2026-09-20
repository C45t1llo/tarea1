class SistemaCalificaciones:
    def __init__(self):
        self.estudiantes = []

    def registrar(self, *estudiantes):
        for estudiante in estudiantes:
            self.estudiantes.append(estudiante)

    def promedio_estudiante(self, nombre):
        for estudiante in self.estudiantes:
            nombre_estudiante, nota1, nota2, nota3 = estudiante

            if nombre_estudiante == nombre:
                promedio = (nota1 + nota2 + nota3) / 3
                return promedio

        return 0

    def aprobados(self):
        aprobados = []

        for estudiante in self.estudiantes:
            nombre, nota1, nota2, nota3 = estudiante
            promedio = (nota1 + nota2 + nota3) / 3

            if promedio >= 7:
                aprobados.append(nombre)

        return aprobados

    def mejor_estudiante(self):
        mejor = None
        mejor_promedio = 0

        for estudiante in self.estudiantes:
            nombre, nota1, nota2, nota3 = estudiante
            promedio = (nota1 + nota2 + nota3) / 3

            if promedio > mejor_promedio:
                mejor_promedio = promedio
                mejor = nombre

        return mejor
sistema = SistemaCalificaciones()

sistema.registrar(
    ("Emanuella", 10, 10, 9),
    ("Paula", 6, 9, 10),
    ("Jefferson", 9, 5, 9),
    ("Amanda", 5, 1, 7)
)
print("Estudiantes:", sistema.estudiantes)
print("Promedio de Emanuella:", sistema.promedio_estudiante("Emanuella"))
print("Aprobados:", sistema.aprobados())
print("Mejor estudiante:", sistema.mejor_estudiante())