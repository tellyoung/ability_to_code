class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxDepth(node):
    if node is None:
        return 0
    else:
        lDepth = maxDepth(node.left)
        rDepth = maxDepth(node.right)

        if lDepth >= rDepth:
            return lDepth + 1
        else:
            return rDepth + 1


def preorder(root):
    if not root: return
    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)


def preorder_non_recursion(root):
    stack = [root]
    res = []
    while stack:
        tmp = stack.pop(-1)
        res.append(tmp.data)
        if tmp.right:
            stack.append(tmp.right)
        if tmp.left:
            stack.append(tmp.left)
    return res


def inorder(root):
    if not root: return
    inorder(root.left)
    print(root.data, end=' ')
    inorder(root.right)


def inorder_non_recursion(root):
    stack, res = [], []
    while stack or root:
        while root:
            stack.append(root)
            root = root.left
        if stack:
            root = stack.pop(-1)
            res.append(root.data)
            root = root.right
    return res


def postOrder(root):
    if not root: return
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end=' ')


def postOrder_non_recursion(root):
    stack = []
    res = []
    while stack or root:
        while root:
            stack.append(root)
            res.append(root.data)
            root = root.right
        if stack:
            root = stack.pop()
            root = root.left
    return res[::-1]


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Height of tree is %d" % (maxDepth(root)))

    preorder(root)
    print(preorder_non_recursion(root))

    inorder(root)
    print(inorder_non_recursion(root))

    postOrder(root)
    print(postOrder_non_recursion(root))