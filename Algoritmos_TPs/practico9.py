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


# Ej 5

def dividir_lista_positivos_negativos(cabeza):
    cabeza_positivos = None
    actual_positivos = None
    cabeza_negativos = None
    actual_negativos = None
    actual = cabeza
    while actual:
        nuevo_nodo = Nodo(actual.dato)
        if actual.dato >= 0:
            if cabeza_positivos is None:
                cabeza_positivos = nuevo_nodo
                actual_positivos = cabeza_positivos
            else:
                actual_positivos.siguiente = nuevo_nodo
                actual_positivos = actual_positivos.siguiente
        else:
            if cabeza_negativos is None:
                cabeza_negativos = nuevo_nodo
                actual_negativos = cabeza_negativos
            else:
                actual_negativos.siguiente = nuevo_nodo
                actual_negativos = actual_negativos.siguiente
        actual = actual.siguiente
    return cabeza_positivos, cabeza_negativos

nodo6 = Nodo(-1)
nodo7 = Nodo(-2)
nodo8 = Nodo(-3)
nodo9 = Nodo(-4)

nodo5.siguiente = nodo6
nodo6.siguiente = nodo7
nodo7.siguiente = nodo8
nodo8.siguiente = nodo9

positivos, negativos = dividir_lista_positivos_negativos(nodo1)
print("Lista de números positivos:")
actual = positivos
while actual:
    print(actual.dato, end=" ")
    actual = actual.siguiente
print()

print("Lista de números negativos:")
actual = negativos
while actual:
    print(actual.dato, end=" ")
    actual = actual.siguiente
print()


#Ej 6

def eliminar_vocales(cabeza):
    vocales = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    nueva_cabeza = None
    nuevo_actual = None
    actual = cabeza
    while actual:
        if actual.dato not in vocales:
            nuevo_nodo = Nodo(actual.dato)
            if nueva_cabeza is None:
                nueva_cabeza = nuevo_nodo
                nuevo_actual = nueva_cabeza
            else:
                nuevo_actual.siguiente = nuevo_nodo
                nuevo_actual = nuevo_actual.siguiente
        actual = actual.siguiente
    return nueva_cabeza

nodo_a = Nodo('a')
nodo_b = Nodo('b')
nodo_c = Nodo('e')
nodo_d = Nodo('d')
nodo_e = Nodo('i')
nodo_f = Nodo('x')

nodo_a.siguiente = nodo_b
nodo_b.siguiente = nodo_c
nodo_c.siguiente = nodo_d
nodo_d.siguiente = nodo_e
nodo_e.siguiente = nodo_f

sin_vocales = eliminar_vocales(nodo_a)
print("Lista sin vocales:")
actual = sin_vocales
while actual:
    print(actual.dato, end=" ")
    actual = actual.siguiente
print()


#Ej 7

def contar_apariciones(s, a):
    contador = 0
    actual = s
    while actual:
        if actual.dato == a:
            contador += 1
        actual = actual.siguiente
    return contador

nodo10 = Nodo(2)
nodo11 = Nodo(2)
nodo12 = Nodo(2)
nodo13 = Nodo(2)
nodo14 = Nodo(2)
nodo15 = Nodo(2)
nodo16 = Nodo(2)

nodo10.siguiente = nodo11
nodo11.siguiente = nodo12
nodo12.siguiente = nodo13
nodo13.siguiente = nodo14
nodo14.siguiente = nodo15
nodo15.siguiente = nodo16


a = int(input("ingrese el nodo a buscar: "))
print(f"El número {a} aparece {contar_apariciones(nodo1, a)} veces en la lista.")