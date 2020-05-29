class Solution:
    def to_sum(slef, x):
        sumx = 0
        while x:
            tmp = x % 10 
            x = x // 10
            sumx = sumx + tmp
        return sumx

    def movingCount(self, m: int, n: int, k: int) -> int:
        count = 1
        see = set([(0, 0)])
        for i in range(m):
            sum_m = self.to_sum(i)
            if sum_m <= k:
                for j in range(n):
                    if ((i - 1, j) in see or (i, j - 1) in see) and(sum_m + self.to_sum(j)) <= k:
                        see.add((i, j))
                        count += 1
        return count

---------------------------------

def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:
        vis = set([(0, 0)])
        for i in range(m):
            for j in range(n):
                if ((i - 1, j) in vis or (i, j - 1) in vis) and digitsum(i) + digitsum(j) <= k:
                    vis.add((i, j))
        return len(vis)
