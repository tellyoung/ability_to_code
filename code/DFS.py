class Solution:
    def __init__(self):
        self.sub_seq = []
        self.nums = []
        self.product_weight = []
        self.product_value = []

    def sub_seq_dfs(self, index, choose=''):
        if index >= len(self.nums):
            if choose:
                self.sub_seq.append(choose)
            return
        self.sub_seq_dfs(index + 1, choose)
        self.sub_seq_dfs(index + 1, choose + str(self.nums[index]))

    def bag01(self, index, sumW, sumV):
        if index == len(self.product_weight):
            return

        if sumW < max_weight:
            if sumV > max_value:
                max_value = sumV
            self.bag01(index + 1, sumW, sumV)
            self.bag01(index + 1, sumW + self.product_weight[index], sumV + self.product_value[index])

if __name__ == "__main__":
    # nums = [1, 2, 3]
    # dfs(0, nums,['xxx'])
    #
    # test = Solution()
    # test.nums = [1, 2, 3]
    # test.sub_seq_dfs(0)
    # print(test.sub_seq)

    # max_weight, max_value = 8, 0
    # test.product_weight = [3, 5, 1, 2, 2]
    # test.product_value= [4, 5, 2, 1, 3]
    # test.bag01(0, 0, 0)

    #print(max_value)


    # product_weight = [3, 5, 1, 2, 2]
    # product_value = [4, 5, 2, 1, 3]
