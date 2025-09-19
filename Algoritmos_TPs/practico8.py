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


#2
pila = []
pila.append("h")
pila.append("o")
pila.append("l")
pila.append("a")
print("Pila original:", pila)

pila_invertida = [] 
while pila: 
    pila_invertida.append(pila.pop())

print("Pila invertida:", pila_invertida) 


#3

pila = []
pila_invertida = []

palabra = input("Ingrese una palabra para verificar si es palíndromo: ")
for letra in palabra:
    pila.append(letra)

temp_pila = pila.copy()
while temp_pila:
    pila_invertida.append(temp_pila.pop())

if pila == pila_invertida:
    print(f"La palabra '{palabra}' es un palíndromo.")
else:
    print(f"La palabra '{palabra}' no es un palíndromo.")