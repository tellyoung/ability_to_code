
def minimumTotal(triangle):
    n = len(triangle)

    def func(idx, j):
        if idx == n:
            res.append(sum(choose))
            return
        for x in [0, 1]:
            if j + x >= len(triangle[idx]):
                continue
            choose.append(triangle[idx][j + x])
            func(idx + 1, j + x)
            choose.pop(-1)

    choose = []
    res = []
    func(0, 0)
    print(res)
    return min(res)


if __name__ == '__main__':
    print(minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))