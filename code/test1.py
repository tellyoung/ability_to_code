n = 3

nums = [[1], [2, 4,5], [3, 6, 7, 8, 9]]

for i in range(n):
    tmp = [0] * (n-1-i)
    nums[i] = tmp + nums[i] + tmp
print(nums)

for i in range(1, n):
    for j in range(len(nums[i])):
        if j == 0:
            nums[i][j] = nums[i][j] + max(nums[i-1][:2])
        elif j == len(nums[i])-1:
            nums[i][j] = nums[i][j] + max(nums[i - 1][-2:])
        else:
            nums[i][j] = nums[i][j] + max(nums[i - 1][j-1:j+2])
print(nums)
print(max(nums[0][1:4]))