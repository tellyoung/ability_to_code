# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(pre, inorder):
            if len(pre) == 0:
                return None
            root = TreeNode(pre[0])
            ind = inorder.index(pre[0])
            root.left = build(pre[1: ind + 1], inorder[0: ind])
            root.right = build(pre[ind + 1: ], inorder[ind + 1: ])
            return root

        if len(preorder) == 0:
            return None
        root = build(preorder, inorder)
        return root