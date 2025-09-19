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