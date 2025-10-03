#Ej 1

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

def contar_nodos(cabeza):
    contador = 0
    actual = cabeza
    while actual is not None:
        contador += 1
        actual = actual.siguiente
    return contador

nodo1 = Nodo(1)
nodo2 = Nodo(2)
nodo3 = Nodo(3)
nodo4 = Nodo(4)
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4

print("Cantidad de nodos:", contar_nodos(nodo1)) 


# Ej 2

def encontrar_posicion(cabeza, valor_buscado):
    posicion = 1
    actual = cabeza
    while actual is not None:
        if actual.dato == valor_buscado:
            return posicion
        actual = actual.siguiente
        posicion += 1
    return -1

nodox = int(input("Ingrese el valor del nodo a buscar: "))

pos = encontrar_posicion(nodo1, nodox)
if pos != -1:
    print(f"El nodo con valor {nodox} está en la posición {pos}.")
else:
    print(f"El nodo con valor {nodox} no se encuentra en la lista.")

