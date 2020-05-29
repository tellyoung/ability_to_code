class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def exist_func(i, j, k):
            flag = False
            if (i, j) in see: 
                return False
            else:
                see[(i, j)] = 1
            if k >= word_len: return True
            if i < 0 or i >= n or j < 0 or j >= m: return False
            if board[i][j] == word[k]: 
                flag = True
            else:
                see.pop((i, j))
            return flag and (exist_func(i + 1, j, k + 1) or exist_func(i - 1, j, k + 1) \
                or exist_func(i, j + 1, k + 1) or exist_func(i, j - 1, k + 1))
        
        n, m, word_len = len(board), len(board[0]), len(word)
        for i in range(0, n):
            for j in range(0, m):
                see = {}
                if board[i][j] == word[0]:
                    if exist_func(i, j, 0):                                                                     
                        return True 
        return False