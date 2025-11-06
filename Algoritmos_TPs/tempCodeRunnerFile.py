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