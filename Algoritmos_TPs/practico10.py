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