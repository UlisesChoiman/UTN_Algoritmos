import math

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


#2

    class Triangulo:
        def __init__(self, lado1, lado2, lado3):
            self.lado1 = lado1
            self.lado2 = lado2
            self.lado3 = lado3

        def perimetro(self):
            return self.lado1 + self.lado2 + self.lado3

        def area(self):
            s = self.perimetro() / 2
            return math.sqrt(s * (s - self.lado1) * (s - self.lado2) * (s - self.lado3))

        def forma(self):
            if self.lado1 == self.lado2 == self.lado3:
                return "Equilátero"
            elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
                return "Isósceles"
            else:
                return "Irregular"
            
    if __name__ == "__main__":
        t = Triangulo(3, 4, 5)
        print(f"Perímetro: {t.perimetro()}")
        print(f"Área: {t.area():.2f}")
        print(f"Forma: {t.forma()}")

