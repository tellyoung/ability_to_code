class Node:
    def __init__(self, name):
        self.name = name
        self.child = {}  # link : node


choose = {'A': ['10'], 'E': ['2', '3']}

theInput = ['A,B,30', 'A,E,10', 'B,C,50', 'B,D,30', 'F,H,0', 'H,I,PIN', 'H,J,IP', 'K,M,30', 'K,N,50', 'E,F,3', 'E,K,2', 'F,G,30']
dic = {}  # str : node

for s in theInput:
    c = s.split(',')
    if c[0] not in dic:
        dic[c[0]] = Node(c[0])
    if c[1] not in dic:
        dic[c[1]] = Node(c[1])
    dic[c[0]].child[c[2]] = dic[c[1]]

# for k in dic:
#     print(k, dic[k].name, dic[k].child)

queue = [dic[list(choose.keys())[0]]]
i, n = 0, len(choose)
res = []

while queue:
    next = []
    for node in queue:
        for k in node.child:
            if node.name in choose:
                if k in choose[node.name]:
                    print(node.child[k].name)
                    next.append(node.child[k])
            else:
                print(node.child[k].name)
                next.append(node.child[k])
        if not node.child:
            res.append(node.name)

    queue = next

print(res)

