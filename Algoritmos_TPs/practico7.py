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



#4

class Planeta: 
    def __init__(self, name = None, cant_satelites = 0, mass = 0, volume = 0, diametro = 0, distancia_sol = 0, tipo_planeta = None, observable = False):
        self.name = name
        self.cant_satelites = cant_satelites
        self.mass = mass
        self.volume = volume
        self.diametro = diametro
        self.distancia_sol = distancia_sol
        self.tipo_planeta = tipo_planeta
        self.observable = observable

    def __str__(self):
        return (f"Planeta: {self.name}, Cantidad de satelites: {self.cant_satelites}, "
                f"Masa: {self.mass} kg, Volumen: {self.volume} km³, Diametro: {self.diametro} km, "
                f"Distancia al sol: {self.distancia_sol} km, Tipo de planeta: {self.tipo_planeta}, "
                f"Observable a simple vista: {self.observable}")

    def densidad(self):
        return self.mass / self.volume if self.volume != 0 else 0

    def planeta_exterior(self):
        UA = 1.496e+11
        return self.tipo_planeta == "Exterior" if self.distancia_sol > 2.1 * UA and self.distancia_sol < 3.4 * UA else False
    
if __name__ == "__main__":
    planeta1 = Planeta("Tierra", 1, 5.972e24, 1.08321e12, 12742, 1.496e90, "Terrestre", True)
    planeta2 = Planeta("Júpiter2", 79, 1.898e27, 1.43128e15, 139820, 7.785e11, "Exterior", False)
    print(planeta1)
    print(f"Densidad: {planeta1.densidad()} kg/km³")
    print(f"¿Es un planeta exterior? {'Sí' if planeta1.planeta_exterior() else 'No'}")
    print()
    print(planeta2)
    print(f"Densidad: {planeta2.densidad()} kg/km³")
    print(f"¿Es un planeta exterior? {'Sí' if planeta2.planeta_exterior() else 'No'}")


#5

class Vehiculo:
    def __init__(self, marca, modelo, patente, color):
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.color = color
        self.autos = []

    def add_auto(self):
        self.autos.append({
            "marca": self.marca,
            "modelo": self.modelo,
            "patente": self.patente,
            "color": self.color
        })
        print(f"Vehículo agregado: {self.marca} {self.modelo}, Patente: {self.patente}, Color: {self.color}")


if __name__ == "__main__":
   for i in range(3):
       marca = input("Ingrese la marca del vehículo: ")
       modelo = input("Ingrese el modelo del vehículo: ")
       patente = input("Ingrese la patente del vehículo: ")
       color = input("Ingrese el color del vehículo: ")
       vehiculo = Vehiculo(marca, modelo, patente, color)
       vehiculo.add_auto()

print("Lista de vehículos:")
for auto in vehiculo.autos:
    print(f"{auto['marca']} {auto['modelo']}, Patente: {auto['patente']}, Color: {auto['color']}")



#6

class Empleado:
    def __init__(self, nombre, horas_trabajadas, tarifa_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora
        self.empleado = []

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_hora

    def agregar_empleado(self):
        self.empleado.append({
            "nombre": self.nombre,
            "horas_trabajadas": self.horas_trabajadas,
            "tarifa_hora": self.tarifa_hora,
            "salario": self.calcular_salario()
        })
        print(f"Empleado agregado: {self.nombre}, Salario: {self.calcular_salario()}")

if __name__ == "__main__":
   n = int(input("Ingrese la cantidad de empleados a agregar: "))
   for i in range(n):
       nombre = input("Ingrese el nombre del empleado: ")
       horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
       tarifa_hora = float(input("Ingrese la tarifa por hora: "))
       empleado = Empleado(nombre, horas_trabajadas, tarifa_hora)
       empleado.agregar_empleado()

print("Lista de empleados:")
for emp in empleado.empleado:
    print(f"{emp['nombre']}, Horas trabajadas: {emp['horas_trabajadas']}, Tarifa por hora: {emp['tarifa_hora']}, Salario: {emp['salario']}")