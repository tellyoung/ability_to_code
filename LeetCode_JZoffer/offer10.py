class Solution:
    def fib(self, n: int) -> int:
        fib_dict = {}
        fib_dict[0] = 0
        fib_dict[1] = 1
        def fib_fun(n):
            if n in fib_dict:
                return fib_dict[n]
            else:
                fib_dict[n] = (fib_fun(n - 1) + fib_fun(n - 2)) % 1000000007
                return fib_dict[n] 
        return fib_fun(n)


class Solution:
    def numWays(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 1
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n] % 1000000007