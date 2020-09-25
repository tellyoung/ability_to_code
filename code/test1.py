nums = [5,6,1,1,1,2,2,3,1]
dic = {}
for n in nums:
    if n not in dic:
        dic[n] = 1
    else:
        dic[n] += 1
dic[5] = [3,6,7]
print(dic)
print(dic.items())
print(sorted(dic.items(), key=lambda x: x[0]))
dic = sorted(dic)
print(dic)

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def ReverseList(pHead):
    l, r = pHead, pHead.next
    while r:
        tmp = r.next
        r.next = l
        if l == pHead:
            l.next = None
        l, r = r, tmp
    return l
