def foo(l, k):
    left = 0
    right: int = len(l) - 1
    while left <= right:
        mid = (left + right) // 2
        if l[mid] > k:
            right = mid - 1
        elif l[mid] < k:
            left = mid + 1
        elif l[mid] == k:
            return mid
    return -1


if __name__ == '__main__':
    l = list(range(13))
    print(l)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(foo(l, 8))  # 8