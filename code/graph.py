def bfs(g):
    first = list(g.keys())[0]
    q, used = [first], []
    while q:
        nextn = []
        for i in q:
            if i not in used:
                used.append(i)
                for j in g[i]:
                    if j not in used:
                        nextn.append(j)
        q = list(nextn)
        print(','.join(q))

    print(list(used))


def dfs(idx, used):
    print(idx, end=' ')
    print(used)
    for i in g[idx]:
        if i not in used:
            used.append(i)
            dfs(i, used)


def edge_count(g):
    sumx = 0
    for n in g:
        sumx += len(g[n])
    print('the number of edge:', sumx // 2)


def is_cyc(idx, used, parent, g):
    for i in g[idx]:
        if i not in used:
            used.append(i)
            if is_cyc(i, used, idx, g):
                return True
        elif i != parent:
            return True
    return False


def is_tree(g):
    start = list(g.keys())[0]
    used = [start]
    if not is_cyc(start, used, '-1', g): return False
    print(used)
    if len(used) == len(g):
        print('is tree')
    else:
        print('not a tree')


if __name__ == '__main__':
    g = {'a': ['b', 'd'], 'b': ['a', 'c', 'e'], 'c': ['b', 'd'], 'd': ['a', 'c', 'f'], 'e': ['b'], 'f': ['d']}
    start = list(g.keys())[0]
    print(start)
    bfs(g)
    dfs(start, [start])

    edge_count(g)  # 无向图边数量

    if is_cyc(start, [start], '-1', g): print('is cycle')  # 图中是否有环

    is_tree(g)