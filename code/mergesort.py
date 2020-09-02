def merge(left, right):
    """
    将两个列表left, right按顺序融合为一个列表res
    """
    res = []
    i, j = 0, 0       # i和j是位置指针，i指left，j指right
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    if i == len(left):
        for x in right[j:]:
            res.append(x)
    else:
        for x in left[i:]:
            res.append(x)

    return res


def merge_sort(arr):
    """
    归并排序
    """
    if len(arr) <= 1: return arr   # 只有一个元素 不用排序
    mid = len(arr) // 2

    left = merge_sort(arr[: mid])  # 子序列递归调用排序
    right = merge_sort(arr[mid:])

    return merge(left, right)


if __name__ == '__main__':
    a = [4, 7, 8, 3, 5, 9]
    print(merge_sort(a))
