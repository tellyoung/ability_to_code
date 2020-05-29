# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []
        pre, end = None, head
        while end:
            tmp = end.next
            end.next = pre
            pre, end = end, tmp
        res = []
        while pre:
            res.append(pre.val)
            pre = pre.next
        return res