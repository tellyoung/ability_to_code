class Solution:

    def cuttingRope(self, n):

        def dfs(index, choose, temp_x):
            nonlocal max_x
            sumx = sum(choose) if choose else 0
            if sumx > n:
                temp_x = 1
                return

            if sumx == n:
                if temp_x > max_x:

                    max_x = temp_x
                print(temp_x)
                temp_x = 1
                return

            for i in range(index, n):
                choose.append(i)
                dfs(i, choose, temp_x * i)
                choose.pop(-1)

        max_x = 1
        dfs(1, [], 1)

        return max_x

if __name__ == '__main__':

    test = Solution()
    test.cuttingRope(10)
