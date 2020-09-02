def insert_sele(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


def bubbling(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print(arr)


def selection(arr):
    for i in range(len(arr) - 1):
        maxn = 0
        for j in range(0, len(arr) - i):
            if arr[maxn] < arr[j]:
                maxn = j
        arr[maxn], arr[len(arr)-1-i] = arr[len(arr)-1-i], arr[maxn]
    print(arr)


def quick(arr, left, right):
    if left >= right:
        return
    n = len(arr)
    low, heigh = left, right
    base = arr[low]
    while low < heigh:
        while arr[heigh] >= base and low < heigh:
            heigh -= 1
        arr[low] = arr[heigh]
        while arr[low] < base and low < heigh:
            low += 1
        arr[heigh] = arr[low]
    arr[low] = base
    quick(arr, left, low - 1)
    quick(arr, low + 1, right)



if __name__ == '__main__':
    arr = [1, 9, 8, 5, 8, 3, 7, 8, 6, 1, 2]
    insert_sele(arr)
    arr = [1, 9, 8, 5, 8, 3, 7, 8, 6, 1, 2]
    print(arr)
    bubbling(arr)
    arr = [1, 9, 8, 5, 8, 3, 7, 8, 6, 1, 2]
    print(arr)
    selection(arr)
    arr = [1, 9, 8, 5, 8, 3, 7, 8, 6, 1, 2]
    print(arr)
    quick(arr, 0, len(arr)-1)
    print('quick', arr)