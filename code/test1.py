n, m = map(int, input().split())
nums = []
for i in range(n):
    num = list(map(int, input().split()))
    nums.append(num)

used = set()
maxn = 0

def dfs(i, j):
    global maxn
    # print(len(used))
    if maxn < len(used):
        maxn = len(used)

    for x in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        tmp = (i + x[0], j + x[1])
        if tmp[0] >= n or tmp[0] < 0 or tmp[1] < 0 or tmp[1] >= m:
            continue
        if tmp not in used and nums[tmp[0]][tmp[1]] < nums[i][j]:
            used.add(tmp)
            dfs(i + x[0], j + x[1])
            used.discard(tmp)

for i in range(n):
    for j in range(m):
        dfs(i, j)

print(maxn + 1)