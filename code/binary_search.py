class Solution:

    def base_search(self, nums, target):
        '''
            实现一个基础二分查找
            输入:一个顺序list
            输出: 待查找的元素的位置
        '''
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target >= nums[mid]:
                left = mid + 1
        return left, right



    def left_search(self, nums, target):
        '''
        查找左边界
        '''
        if not nums: return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left+right) >> 1
            if nums[mid] == target:
                right = mid - 1
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        if left >= len(nums) or nums[left] != target:
            return -1

        return left


if __name__ == "__main__":
    test = Solution()
    nums = [0, 1, 2, 3, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10]

    print(nums)
    print([i for i in range(len(nums))])
    res = test.base_search(nums, 3)
    print(res)
    # print(test.left_search([-1, 0, 2, 2, 2, 3, 4], 2))
