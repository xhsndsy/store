
def bubble_sort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array) - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == '__main__':
    a = [5, 2, 4, 7, 9, 1, 3, 5, 4, 0, 6, 1, 3]
    print(bubble_sort(a))