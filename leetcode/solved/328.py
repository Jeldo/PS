'''
Category: Linked List
Time Complexity: O(n)
Space Complexity: O(1)

switching odd-even nodes
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def showNodeValues(head: ListNode):
    while head:
        print(head.val, end=' ')
        head = head.next
    print()


class Solution:
    def oddEvenList(self, head: ListNode):
        count = 0
        even_prev = ListNode(None)
        odd_prev = ListNode(None)
        even_head = head
        odd_head = odd_prev
        even_last = ListNode(None)
        while head:
            if count % 2 == 0:
                even_prev = head
                even_last = head
                odd_prev.next = head.next
            else:
                odd_prev = head
                even_prev.next = head.next
            count += 1
            head = head.next
        even_last.next = odd_head.next
        # showNodeValues(odd_head)
        return even_head


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e


aa = ListNode(2)
bb = ListNode(1)
cc = ListNode(3)
dd = ListNode(5)
ee = ListNode(6)
ff = ListNode(4)
gg = ListNode(7)
aa.next = bb
bb.next = cc
cc.next = dd
dd.next = ee
ee.next = ff
ff.next = gg


aaa = ListNode(1)
bbb = ListNode(2)
ccc = ListNode(3)
ddd = ListNode(4)
eee = ListNode(5)
fff = ListNode(6)
ggg = ListNode(7)
hhh = ListNode(8)
aaa.next = bbb
bbb.next = ccc
ccc.next = ddd
ddd.next = eee
eee.next = fff
fff.next = ggg
ggg.next = hhh

cases = [
    a,
    aa,
    aaa
]

for case in cases:
    s = Solution().oddEvenList(case)
    showNodeValues(s)
    # print(s)
