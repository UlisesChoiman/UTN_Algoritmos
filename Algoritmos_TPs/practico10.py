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