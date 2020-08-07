class Solution:
    def __init__(self):
        self.nums = []
        self.res_sub_seq = []

        self.product_weight = []
        self.product_value = []
        self.max_value = 0
        self.max_weight = 8

        self.res_full_per = []

        self.direction = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def sub_seq_dfs(self, index, choose=[]):
        """
        通过dfs寻找全部子序列
        :param index: 数字序号
        :param choose: 当前子序列
        :return: none
        """
        if index == len(self.nums):
            if choose:
                print(choose)
                self.res_sub_seq.append(choose.copy())
            return

        self.sub_seq_dfs(index + 1, choose)  # 不选index

        choose.append(self.nums[index])
        self.sub_seq_dfs(index + 1, choose)  # 选index
        choose.pop(-1)  # 选index的路径结束回到分叉点

    def bag01(self, index, sumW, sumV):
        """
        01背包问题dfs解法
        :param index: 产品序号
        :param sumW: 当前重量
        :param sumV: 当前价值
        :return:
        """
        if index == len(self.product_weight):
            if sumW <= self.max_weight and sumV > self.max_value:
                self.max_value = sumV
            return

        self.bag01(index + 1, sumW, sumV)
        self.bag01(index + 1, sumW + self.product_weight[index], sumV + self.product_value[index])

    def full_permutation(self, nums=[1, 2, 3]):
        """
        全排列 没有相同元素
        :param nums: 待排数组
        :return: res[]
        """
        def dfs(index, choose):
            if index == size:
                res.append(choose.copy())
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    choose.append(nums[i])
                    dfs(index + 1, choose)
                    used[i] = False
                    choose.pop()

        res, size = [], len(nums)
        used = [False] * size
        dfs(0, [])
        return res


    def full_permut(self, nums=[1,2,1]):
        def dfs(index, choose):
            if index == size:
                res.append(choose.copy())
                return

            for i in range(size):
                if not used[i]:
                    if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                        # not used 其实排在前面的相同元素已经被选中过的意思
                        continue

                    used[i] = True
                    choose.append(nums[i])
                    dfs(index + 1, choose)
                    used[i] = False
                    choose.pop()

        nums.sort()
        res, size = [], len(nums)
        used = [False] * size
        dfs(0, [])
        return res

    def path_search(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0: return False
        n, m = len(board), len(board[0])
        used = [[False for i in range(m)] for j in range(n)]

        for i in range(n):
            for j in range(m):
                if self.__search_word(board, word, i, j, used, 0, n, m):
                    return True

        return False

    def __search_word(self, board, word, i, j, used, idx, n, m):
        if idx == len(word) - 1:
            return board[i][j] == word[idx]

        if board[i][j] == word[idx]:
            used[i][j] = True
            for d in self.direction:
                new_i = i + d[0]
                new_j = j + d[1]
                if 0 <= new_i < n and 0 <= new_j < m and not used[new_i][new_j] and \
                        self.__search_word(board, word, new_i, new_j, used, idx + 1, n, m):
                    return True

            used[i][j] = False

        return False




if __name__ == "__main__":
    test = Solution()
    test.nums = [1, 2, 3]
    test.sub_seq_dfs(0)

    test.product_weight = [3, 5, 1, 2, 2]
    test.product_value = [4, 5, 2, 1, 3]
    test.bag01(0, 0, 0)
    print('the max value: ', test.max_value)

    print(test.full_permutation())
    print(test.full_permut())