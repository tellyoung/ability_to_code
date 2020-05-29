class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        n, m = len(matrix) - 1, len(matrix[0]) - 1
        tN , tM = 0, m
        while tN <= n and tM >= 0:
            if matrix[tN][tM] == target:
                return True
            elif matrix[tN][tM] > target:
                tM -= 1
            else:
                tN += 1
        return False