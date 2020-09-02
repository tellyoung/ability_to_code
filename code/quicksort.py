def quick_sort(arr, start, end):
    """
    快速排序
    """
    if start >= end:
        return

    base = arr[start]  # 设定基准元素
    low, high = start, end

    while low < high:
        while low < high and arr[high] >= base:
            high -= 1
        arr[low] = arr[high] # high指向一个比基准元素小的元素,将high指向的元素放到low的位置上
        # 此时high指向的位置空着,接下来移动low找到符合条件的元素放在此处

        while low < high and arr[low] < base: # low指向的元素比基准元素小，则low向右移动
            low += 1
        arr[high] = arr[low]  # 此时low指向一个比基准元素大的元素,将low指向的元素放到high空着的位置上,此时low指向的位置空着,之后进行下一次循环,将high找到符合条件的元素填到此处

    # 退出循环后，low与high重合
    arr[low] = base  # 将基准元素放到该位置,左边的元素都比基准元素小,右边的元素都比基准元素大

    quick_sort(arr, start, low - 1)
    quick_sort(arr, low + 1, end)


if __name__ == '__main__':
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20,1,2,3,4,5,8,9,565]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)


