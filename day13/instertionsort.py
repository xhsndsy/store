def insertionSort(arr):
    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
insertionSort(arr)
print(insertionSort(arr))