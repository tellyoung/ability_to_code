
def dfs(cur):
    for next in graph[cur]:
        if next not in used:
            used.append(next)
            dfs(next)


def bfs(cur):
    queue = [cur]
    while queue:
        next = []
        for item in queue:
            if item not in used:
                used.append(item)
            for n in graph[item]:
                if n not in used:
                    next.append(n)
        queue = next


if __name__ == '__main__':
    graph = {}
    graph['a'] = ['b', 'c']
    graph['b'] = ['a', 'c']
    graph['c'] = ['a', 'b', 'd']
    graph['d'] = ['c']
    graph['e'] = ['f']
    graph['f'] = ['e']
    print(graph)
    s = set()
    for k in graph.keys():
        s.add(k)
    print(s)
    res = set()

    for cur in s:
        used = [cur]
        dfs(cur)
        used = tuple(sorted(used))
        res.add(used)

    print(res)

    for cur in s:
        used = []
        bfs(cur)
        used = tuple(sorted(used))
        res.add(used)
    print(res)