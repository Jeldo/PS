'''
Category: Linked List
Time Complexity: O(n), sum of iteration in for~while is always O(n).
Space Complexity: O(n)

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
    def splitListToParts(self, root: ListNode, k: int):
        curr, length = root, 0
        while curr:
            curr, length = curr.next, length + 1
        part_len, extra = divmod(length, k)
        parts = [part_len + 1] * extra + [part_len] * (k - extra)
        prev, curr = None, root
        for index, num in enumerate(parts):
            if prev:
                prev.next = None
            parts[index] = curr
            for i in range(num):
                prev, curr = curr, curr.next
        return parts

    def splitListToParts2(self, root: ListNode, k: int):
        ans = list()
        curr, length = root, 0
        while curr:
            curr, length = curr.next, length + 1
        part_len, extra = divmod(length, k)
        index = 0
        while index < k and root:
            ans.append(root)
            j = 1
            while j < part_len + (index < extra):
                root = root.next
                j += 1
            next_node = root.next
            root.next = None
            root = next_node
            index += 1
        # for n in ans:
        #     showNodeValues(n)
        return ans

    def splitListToParts3(self, root: ListNode, k: int):
        nodes = list()
        ans = list()
        while root:
            nodes.append(root)
            root = root.next
        part_len, remainder = divmod(len(nodes), k)
        parts = [part_len for _ in range(k)]
        for i in range(remainder):
            parts[i] += 1
        index = 0
        for part_len in parts:
            if part_len == 0:
                ans.append(None)
            part_count = 0
            while part_count < part_len:
                cur = nodes[index]
                if part_count == 0:
                    ans.append(cur)
                part_count += 1
                if part_count == part_len:
                    cur.next = None
                index += 1
        # for n in ans:
        #     showNodeValues(n)
        return ans


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c


aa = ListNode(1)
bb = ListNode(2)
cc = ListNode(3)
dd = ListNode(4)
ee = ListNode(5)
ff = ListNode(6)
gg = ListNode(7)
hh = ListNode(8)
ii = ListNode(9)
jj = ListNode(10)
aa.next = bb
bb.next = cc
cc.next = dd
dd.next = ee
ee.next = ff
ff.next = gg
gg.next = hh
hh.next = ii
ii.next = jj


aaa = ListNode(1)
bbb = ListNode(2)
ccc = ListNode(3)
ddd = ListNode(4)
eee = ListNode(5)
fff = ListNode(6)
ggg = ListNode(7)
# hhh = ListNode(8)
aaa.next = bbb
bbb.next = ccc
ccc.next = ddd
ddd.next = eee
eee.next = fff
fff.next = ggg
# ggg.next = hhh


cases = [
    [a, 5],
    [aa, 3],
    [aaa, 4],
    [None, 3]
]

for case in cases:
    s = Solution().splitListToParts2(case[0], case[1])
    # showNodeValues(s)
    print(s)
