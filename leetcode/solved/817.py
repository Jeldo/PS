class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def numComponents(self, head: ListNode, G):
        node = head
        set_G = set(G)
        count = list()
        sub = 0
        while node:
            if node.val in set_G:
                sub += 1
                if not node.next:
                    count.append(sub)
            else:
                if sub > 0:
                    count.append(sub)
                sub = 0
            node = node.next
        return len(count)


a = ListNode(0)
b = ListNode(1)
c = ListNode(2)
d = ListNode(3)
e = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = e

arr = [0, 3, 1, 4]

c1 = [a, arr]

aa = ListNode(3)
bb = ListNode(4)
cc = ListNode(0)
dd = ListNode(2)
ee = ListNode(1)
aa.next = bb
bb.next = cc
cc.next = dd
dd.next = ee

arr2 = [4]

c2 = [aa, arr2]

cases = [c1, c2]

for case in cases:
    s = Solution().numComponents(case[0], case[1])
    print(s)
