class Solution:
    def cuttingRope(self, n: int) -> int:
        # 初始化-由于下标的原因又要取到n所以+1
        dp = [1]*(n+1)
        # 外层遍历获取之前的动态结果，目的是为了获取n的动态结果
        
        for each_n in range(2, n+1):
            # 内层循环用来割绳子，从1割到each_n，目的是获取割一遍绳子来获取最大值
            # 也就是穷举出所有可能
            for cut_len in range(1, each_n):
                # 这里用cut_len * dp[each_n-cut_len] 或者 dp[cut_len] * (each_n-cut_len)是一样的
                # 为啥二者都行？其实很简单，cut_len和each_n-cut_len是互补的，循环一遍后都取到了
                dp[each_n] = max(cut_len*dp[each_n-cut_len], cut_len*(each_n-cut_len), dp[each_n])
        return dp[n]

class Solution:
    def cuttingRope(self, n: int) -> int:
        dp = [1] * (n + 1)
        for i in range(0, n + 1):
            for tmp in range(1, i):
                dp[i] = max(dp[i - tmp] * tmp, tmp * (i - tmp), dp[i])
        return dp[n] % 1000000007