class Solution:

    def base_search(self, nums, target) -> int:
        '''
            实现一个基础二分查找
            输入:一个顺序list
            输出: 待查找的元素的位置
        '''
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2  # (left + right) >> 1 除2 向下取整
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
        return -1


    def left_search(self, nums, target):
        '''
        查找左边界
        :param nums: list
        :param target: int
        :return: index
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
    print(test.base_search([-1, 0, 1, 2, 3, 4], 2))
    print(test.left_search([-1, 0, 2, 2, 2, 3, 4], 2))