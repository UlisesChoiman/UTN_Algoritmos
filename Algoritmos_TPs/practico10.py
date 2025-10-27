import random
import array

#1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Lista original
numbers = [76, 21, 34, 68, 31, 27, 53]
print("Lista original:", numbers)

insertion_sort(numbers)
print("Lista ordenada:", numbers)


#2

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Lista original
numbers2 = [6, 2, 4, 8, 3, 7, 5]
print("\nLista original:", numbers2)

selection_sort(numbers2)
print("Lista ordenada:", numbers2)


#3

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

numbers3 = []
for i in range(6):
    num = int(input(f"Ingrese el número {i+1}: "))
    numbers3.append(num)

numbers_insertion = numbers3.copy()
numbers_selection = numbers3.copy()
numbers_bubble = numbers3.copy()

print("\nLista original:", numbers3)

# Ordenar con los tres métodos
insertion_sort(numbers_insertion)
print("Ordenado por inserción:", numbers_insertion)

selection_sort(numbers_selection)
print("Ordenado por selección:", numbers_selection)

bubble_sort(numbers_bubble)
print("Ordenado por burbuja:", numbers_bubble)


#4

# with open('nros.txt', 'w') as f:
    #for _ in range(50):
        #f.write(f"{random.randint(1, 1000)}\n")


#numbers = []
#with open('nros1.txt', 'r') as f:
    #for line in f:
        #numbers.append(int(line.strip()))

#insertion_sort(numbers)

# Escribir números ordenados en nuevo archivo
#with open('ordenado.txt', 'w') as f:
    #for num in numbers:
        #f.write(f"{num}\n")


#5
def insertion_sort_array(arr):
    n = len(arr)
    sorted_arr = array.array(arr.typecode, arr)
    for i in range(1, n):
        key = sorted_arr[i]
        j = i - 1
        while j >= 0 and sorted_arr[j] > key:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        sorted_arr[j + 1] = key
    return sorted_arr

numbers_array = array.array('i', [76, 21, 34, 68, 31, 27, 53])
sorted_array = insertion_sort_array(numbers_array)
print("Array ordenado:", sorted_array)


#6

random_numbers = [random.randint(1, 100) for _ in range(10)]
print("\nArreglo original:", random_numbers)

numbers_ins = random_numbers.copy()
numbers_sel = random_numbers.copy()
numbers_bub = random_numbers.copy()

insertion_sort(numbers_ins)
print("Ordenado por inserción:", numbers_ins)

selection_sort(numbers_sel)
print("Ordenado por selección:", numbers_sel)

bubble_sort(numbers_bub)
print("Ordenado por burbuja:", numbers_bub)


#7

precios = []
for i in range(10):
    while True:
        try:
            entrada = input(f"Ingrese el precio de la golosina {i+1}: ").strip()
            precio = float(entrada.replace(',', '.'))
            precios.append(precio)
            break
        except ValueError:
            print("Entrada inválida. Ingrese un número válido (por ejemplo 12.50).")

print("\nPrecios ingresados:", precios)

precios_insertion = precios.copy()
precios_selection = precios.copy()

insertion_sort(precios_insertion)
selection_sort(precios_selection)

print("\nOrdenado de menor a mayor (insertion sort):", precios_insertion)
print("Ordenado de menor a mayor (selection sort):", precios_selection)


#8

random_list = [random.randint(1, 100) for _ in range(6)]
random_array = array.array('i', [random.randint(1, 100) for _ in range(6)])

print("\nLista original:", random_list)
print("Array original:", random_array)

list_insertion = random_list.copy()
list_bubble = random_list.copy()
insertion_sort(list_insertion)
bubble_sort(list_bubble)

print("\nLista ordenada (insertion sort):", list_insertion)
print("Lista ordenada (bubble sort):", list_bubble)

array_insertion = insertion_sort_array(random_array)
array_selection = array.array('i', random_array)
selection_sort(array_selection)

print("\nArray ordenado (insertion sort):", array_insertion)
print("Array ordenado (selection sort):", array_selection)


#9

import numpy as np

A = np.random.randint(0, 100, size=(2, 3)) #4, 6
print("Matriz original A:")
print(A)

# Ordenar cada fila
O = np.sort(A, axis=1)
print("\nMatriz ordenada por filas O:")
print(O)


#10

with open('pacientes.txt', 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()


pacientes = []
for linea in lineas:
    linea = linea.strip() 
    if linea: 
        datos = [dato.strip() for dato in linea.split(',')]
        # Convertir edad a entero para ordenar correctamente
        datos[2] = int(datos[2])
        pacientes.append(datos)


pacientes_ordenados = sorted(pacientes, key=lambda x: x[2])


print("Pacientes ordenados por edad:")
print("-" * 50)
for paciente in pacientes_ordenados:
    print(f"{paciente[0]}, {paciente[1]}, {paciente[2]}, {paciente[3]}")

# Guardar en nuevo archivo
with open('pacientes_por_edad.txt', 'w', encoding='utf-8') as archivo_salida:
    for paciente in pacientes_ordenados:
        # Convertir edad de nuevo a string para guardar
        linea = f"{paciente[0]}, {paciente[1]}, {paciente[2]}, {paciente[3]}\n"
        archivo_salida.write(linea)

print("\nDatos guardados en 'pacientes_por_edad.txt'")


#11

notas = []
for i in range(10):
    while True:
        try:
            nota = float(input(f"Ingrese la nota del alumno {i+1}: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("La nota debe estar entre 0 y 10")
        except ValueError:
            print("Por favor ingrese un número válido")

notas_ordenadas = notas.copy()
insertion_sort(notas_ordenadas)

print(f"\nPeor nota: {notas_ordenadas[0]}")
print(f"Mejor nota: {notas_ordenadas[-1]}")


#12

nombres = []
for i in range(10):
    nombre = input(f"Ingrese el nombre {i+1}: ").strip()
    nombres.append(nombre)

print("\nNombres originales:", nombres)

nombres_ordenados = sorted(nombres, key=lambda s: len(s))
print("\nNombres ordenados por longitud:")
for n in nombres_ordenados:
    print(n)