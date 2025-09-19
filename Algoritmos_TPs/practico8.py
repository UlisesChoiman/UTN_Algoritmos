class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        return self.items.pop()

    def ver_tope(self):
            return self.items[-1]

    def tamano(self):
        return len(self.items)

    def mostrar(self):
        return self.items


#1
pila = Pila()
pila.apilar(1)
pila.apilar(2)
pila.apilar(3)

print("Pila original:", pila.mostrar())

# Invertir la pila
pila_invertida = Pila()
while not pila.esta_vacia():
    pila_invertida.apilar(pila.desapilar())

print("Pila invertida:", pila_invertida.mostrar())


#2
pila = Pila()
pila.apilar("h")
pila.apilar("o")
pila.apilar("l")
pila.apilar("a")
print("Pila original:", pila.mostrar())

pila_invertida = Pila()
while not pila.esta_vacia():
    pila_invertida.apilar(pila.desapilar())

print("Pila invertida:", pila_invertida.mostrar())


#3
palabra = input("Ingrese una palabra para verificar si es palíndromo: ")
pila = Pila()
pila_invertida = Pila()

for letra in palabra:
    pila.apilar(letra)


temp_pila = Pila()
while not pila.esta_vacia():
    temp_pila.apilar(pila.desapilar())

while not temp_pila.esta_vacia():
    pila_invertida.apilar(temp_pila.desapilar())

if list(palabra) == pila_invertida.mostrar():
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")


#4
pueblos = ["A", "B", "C", "D", "E"] 

camino_ida = Pila()
for pueblo in pueblos:
    camino_ida.apilar(pueblo)

print("Camino de ida:", camino_ida.mostrar())

camino_vuelta = Pila()
while not camino_ida.esta_vacia():
    camino_vuelta.apilar(camino_ida.desapilar())

print("Camino de vuelta:", camino_vuelta.mostrar())


#5
cadena = input("Ingrese una cadena para verificar el balance de paréntesis: ")
pila = Pila()
error = None

for i, simbolo in enumerate(cadena):
    if simbolo == '(':
        pila.apilar(i)
    elif simbolo == ')':
        if pila.esta_vacia():
            error = f"Error en la posición {i}: falta '(' antes de ')'"
            break
        else:
            pila.desapilar()

if error:
    print(error)
elif not pila.esta_vacia():
    print(f"Error: falta ')' para el/los '(' en las posiciones {pila.mostrar()}")
else:
    print("Los paréntesis están correctamente balanceados.")


#6
class Almacen:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pila = Pila()

    def push(self, id_contenedor):
        if self.pila.tamano() < self.capacidad:
            self.pila.apilar(id_contenedor)
        else:
            print("Almacén lleno. No se puede apilar más contenedores.")

    def pop(self, id_contenedor):
        temp = Pila()
        encontrado = False
        while not self.pila.esta_vacia():
            actual = self.pila.desapilar()
            if actual == id_contenedor:
                encontrado = True
                break
            else:
                temp.apilar(actual)
        if not encontrado:
            print(f"Contenedor {id_contenedor} no encontrado.")
        while not temp.esta_vacia():
            self.pila.apilar(temp.desapilar())

almacen = Almacen(5)
almacen.push(101)
almacen.push(102)
almacen.push(103)
almacen.push(104)
almacen.push(105)
print("Contenedores apilados:", almacen.pila.mostrar())

almacen.pop(103)
print("Contenedores después de retirar 103:", almacen.pila.mostrar())


#7
nombre_archivo = input("Ingrese el nombre del archivo de texto a invertir: ")

try:
    with open(nombre_archivo, "r", encoding="utf-8") as archivo:
        lineas = archivo.readlines()

    with open("invertido.txt", "w", encoding="utf-8") as archivo_invertido:
        for linea in reversed(lineas):
            archivo_invertido.write(linea)
    print("Archivo invertido.txt generado correctamente.")
except FileNotFoundError:
    print("El archivo especificado no existe.")


#8
def invertir_palabra_de_frase(frase):
    palabras = frase.split()
    frase_invertida = " ".join(reversed(palabras))
    return frase_invertida
frase = input("Ingrese una frase para invertir: ")
print("Frase invertida:", invertir_palabra_de_frase(frase))


#9
class Paciente:
    def __init__(self, nombre, tiene_obra_social):
        self.nombre = nombre
        self.tiene_obra_social = tiene_obra_social

    def __repr__(self):
        return f"{self.nombre} ({'Obra social' if self.tiene_obra_social else 'Sin obra social'})"

class SalaEspera:
    def __init__(self):
        self.pacientes = []

    def agregar_paciente(self, paciente):
        self.pacientes.append(paciente)

    def atender_pacientes(self):
        cantidad_obra_social = 0
        while self.pacientes:
            paciente = self.pacientes.pop(0)
            print(f"Atendiendo a: {paciente.nombre}")
            if paciente.tiene_obra_social:
                cantidad_obra_social += 1
        print(f"Cantidad de pacientes con obra social: {cantidad_obra_social}")

sala = SalaEspera()

sala.agregar_paciente(Paciente("Ana", True))
sala.agregar_paciente(Paciente("Luis", False))
sala.agregar_paciente(Paciente("María", True))
sala.agregar_paciente(Paciente("Pedro", False))
sala.agregar_paciente(Paciente("Sofía", True))

print("Cola de espera:", sala.pacientes)
sala.atender_pacientes()


#10
class Carta:
    def __init__(self, nombre):
        self.nombre = nombre

class Persona:
    def __init__(self, nombre, cartas):
        self.nombre = nombre
        self.cartas = cartas

class Correo:
    def __init__(self, max_cartas_por_persona=5):
        self.max_cartas_por_persona = max_cartas_por_persona
        self.cola = []

    def agregar_persona(self, persona):
        self.cola.append(persona)

    def atender_persona(self):
        if self.cola:
            persona = self.cola.pop(0)
            cartas_a_recibir = persona.cartas[:self.max_cartas_por_persona]
            cartas_restantes = persona.cartas[self.max_cartas_por_persona:]
            print(f"Atendiendo a {persona.nombre}:")
            for carta in cartas_a_recibir:
                print(f"  Recibida {carta.nombre}")
            if cartas_restantes:
                print(f"{persona.nombre} debe volver a la cola con {len(cartas_restantes)} carta(s) restante(s).")
                self.agregar_persona(Persona(persona.nombre, cartas_restantes))
        else:
            print("No hay personas en la cola.")


correo = Correo(max_cartas_por_persona=3) 

correo.agregar_persona(Persona("Ana", [Carta(f"Carta {i+1}") for i in range(2)]))
correo.agregar_persona(Persona("Luis", [Carta(f"Carta {i+1}") for i in range(5)]))
correo.agregar_persona(Persona("Maria", [Carta(f"Carta {i+1}") for i in range(4)]))

while correo.cola:
    correo.atender_persona()

#11
def simular_cola_impresion(jobs):
    cola = jobs.copy()
    while cola:
        trabajo = cola.pop(0)
        print(f"Imprimiendo '{trabajo['documento']}' ({trabajo['paginas']} paginas)")

trabajos = [
    {'documento': 'Informe.pdf', 'paginas': 10},
    {'documento': 'Factura.docx', 'paginas': 2},
    {'documento': 'Presentacion.pptx', 'paginas': 15}
]

simular_cola_impresion(trabajos)