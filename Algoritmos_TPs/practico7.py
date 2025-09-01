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


#3

class Persona:

        def __init__(self, name="", surname="", age=0, DNI=""):
            self.name = name
            self.surname = surname
            self.age = age
            self.DNI = DNI

        def mostrar(self):
            print(f"Nombre: {self.name} {self.surname}, Edad: {self.age}, DNI: {self.DNI}")

        def es_mayor_de_edad(self):
            return True if self.age >= 18 else False
        

if __name__ == "__main__":
    p1 = Persona("Juan", "Pérez", 20, "12345678A")
    p2 = Persona("Ana", "Gómez", 16, "87654321B")
    p1.mostrar()
    p2.mostrar()
    print(f"¿Es mayor de edad? {'Sí' if p1.es_mayor_de_edad() else 'No'}")
    print(f"¿Es mayor de edad? {'Sí' if p2.es_mayor_de_edad() else 'No'}")

