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
nodo5 = Nodo(5)
nodo1.siguiente = nodo2
nodo2.siguiente = nodo3
nodo3.siguiente = nodo4
nodo4.siguiente = nodo5

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

# Ej 3

def eliminar_penultimo(cabeza):
    if cabeza is None or cabeza.siguiente is None:
        return cabeza  # No hay penúltimo nodo

    anterior = None
    actual = cabeza
    while actual.siguiente and actual.siguiente.siguiente:
        anterior = actual
        actual = actual.siguiente

    if anterior is None:
        cabeza = cabeza.siguiente
    else:
        anterior.siguiente = actual.siguiente
    return cabeza

nodo1 = eliminar_penultimo(nodo1)
actual = nodo1
print("Lista después de eliminar el penúltimo nodo:")
while actual:
    print(actual.dato, end=" ")
    actual = actual.siguiente
print()


# Ej 4
def filtrar_impares(cabeza):
    nueva_cabeza = None
    nuevo_actual = None
    actual = cabeza
    while actual:
        if actual.dato % 2 != 0:
            nuevo_nodo = Nodo(actual.dato)
            if nueva_cabeza is None:
                nueva_cabeza = nuevo_nodo
                nuevo_actual = nueva_cabeza
            else:
                nuevo_actual.siguiente = nuevo_nodo
                nuevo_actual = nuevo_actual.siguiente
        actual = actual.siguiente
    return nueva_cabeza

impares = filtrar_impares(nodo1)
print("Lista de nodos impares:")
actual = impares
while actual:
    print(actual.dato, end=" ")
    actual = actual.siguiente
print()