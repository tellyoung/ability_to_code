[toc]
# Road

# python语法

## 内置函数
```python
abs(x) # 绝对值
```

## 队列

# 排序

## 归并排序

「归并排序」是分治思想的典型应用，它包含这样三个步骤：
>分解:  待排序的区间分成左右两个子序列
>递归: 使用归并排序递归排序子序列 
>合并: 将排好序的子序列合并


```python
def mergeSort(nums, start, end):
    if start >= end: return
    mid = (start + end) // 2
    mergeSort(nums, start, mid)
    mergeSort(nums, mid + 1, end)
    merge(nums, start, mid,  end)

def merge(nums, start, mid, end):
    i, j, temp = start, mid + 1, []
    while i <= mid and j <= end:
	    if nums[i] <= nums[j]:
    		temp.append(nums[i])
    		i += 1
    	else:
            temp.append(nums[j])
    		j += 1
        while i <= mid:
            temp.append(nums[i])
            i += 1
        while j <= end:
            temp.append(nums[j])
            j += 1

        for i in range(len(temp)):
        	nums[start + i] = temp[i]
		temp.clear()
```

# 位运算

1. 相同的两个数字相互异或，值为0

```python
a ^= b # 异或操作
a & b # 与操作
a << 1 # 二进制左移一位
```

