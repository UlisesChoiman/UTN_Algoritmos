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