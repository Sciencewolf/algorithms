def binary_search(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid

    return -1

def find_(arr, x):
    if x > len(arr):
        return -1

    i = 0
    while i < len(arr) and x > arr[i]:
        i += 1

    if arr[i] == x:
        return i
    else:
        return -1


def bubble_sort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


if __name__ == '__main__':
    from random import randint

    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(arr, 5))
    print(find_(arr, 11))

    arr = list(range(1, 1_000_000))

    for i, _ in enumerate(arr):
        arr[i] = arr[i - 1] + randint(1, 10 ** 6)

    print(binary_search(arr, 5_000))

    a = [1, 3, 2, 4, 5, 5, 1, 2]

    bubble_sort(a)
