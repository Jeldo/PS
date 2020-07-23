'''
Category: Stack, Linked List
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nextLargerNodes(self, head: ListNode):
        answer = []

        return


cases = [
    [2, 1, 5],
    [2, 7, 4, 3, 5],
    [1, 7, 5, 1, 9, 2, 5, 1]
]

for c in cases:
    head = None
    temp_next = None
    for n in reversed(c):
        head = ListNode(n, temp_next)
        temp_next = head
    s = Solution().nextLargerNodes(head)
    print(s)
