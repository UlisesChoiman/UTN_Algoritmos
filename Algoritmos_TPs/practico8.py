#1

pila = []
pila.append(1)
pila.append(2)
pila.append(3)

print("Pila original:", pila)

# Invertir la pila
pila_invertida = []
while pila:
    pila_invertida.append(pila.pop())

print("Pila invertida:", pila_invertida)