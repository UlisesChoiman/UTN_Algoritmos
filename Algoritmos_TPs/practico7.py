#1
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        print(f"Nombre: {self.nombre}, Nota: {self.nota}")

    def resultado(self):
        if self.nota >= 6:
            print(f"{self.nombre} ha aprobado con una nota de {self.nota}.")
        else:
            print(f"{self.nombre} no ha aprobado. Nota: {self.nota}.")

if __name__ == "__main__":
    alumno1 = Alumno("Juan", 7)
    alumno2 = Alumno("Ana", 5)
    alumno1.imprimir()
    alumno1.resultado()
    alumno2.imprimir()
    alumno2.resultado()
