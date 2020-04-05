'''
Category: Linked List
Time Complexity: 
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution:
    def nextLargerNodes(self, head: ListNode):
        ans = list()
        # stack = list()
        # cur = head
        # while cur.next:
        #     stack.append(cur.val)
        #     cur = cur.next
        # stack.append(cur.val)

        # highest = 0
        # while stack:
        #     val = stack.pop()
        #     if highest < val:
        #         highest = val
        #         ans.insert(0, 0)
        #     else:
        #         ans.insert(0, highest)
        nodes = list()

        def dfs(node: ListNode):
            if node:
                nodes.append(node)
            if node.next:
                dfs(node.next)
        dfs(head)
        return ans

    # brute force, time limit exceeds
    def nextLargerNodes2(self, head: ListNode):
        def dfs(node: ListNode, origin: ListNode):
            if not node.next:
                ans.append(0)
            else:
                if origin.val < node.next.val:
                    ans.append(node.next.val)
                    return
                dfs(node.next, origin)

        ans = list()
        if not head:
            return [0]
        else:
            cur_node = head
            while cur_node:
                dfs(cur_node, cur_node)
                cur_node = cur_node.next
        return ans


a = ListNode(2)
b = ListNode(1)
c = ListNode(5)
a.next = b
b.next = c

aa = ListNode(1)
bb = ListNode(7)
cc = ListNode(5)
dd = ListNode(1)
ee = ListNode(9)
ff = ListNode(2)
gg = ListNode(5)
hh = ListNode(1)

aa.next = bb
bb.next = cc
cc.next = dd
dd.next = ee
ee.next = ff
ff.next = gg
gg.next = hh

cases = [
    a,
    aa
]

for c in cases:
    s = Solution().nextLargerNodes(c)
    print(s)
