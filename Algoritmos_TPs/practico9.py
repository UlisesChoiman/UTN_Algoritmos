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
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3

print("Cantidad de nodos:", contar_nodos(nodo1))  # Salida: 3