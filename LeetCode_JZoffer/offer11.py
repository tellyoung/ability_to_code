class Solution:
    def minArray(self, numbers: List[int]) -> int:
        n = len(numbers)
        if n == 0: return []
        if n == 1: return numbers[0] 
        pre, end = 0, 1
        while end < n:
            if numbers[pre] <= numbers[end]:
                pre, end = end, end + 1
            else:
                return numbers[end]
        return numbers[0]

# 二分法
class Solution:
    def minArray(self, numbers: [int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]: i = m + 1
            elif numbers[m] < numbers[j]: j = m
            else: j -= 1
        return numbers[i]
