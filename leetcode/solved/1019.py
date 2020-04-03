# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def nextLargerNodes(self, head):
        return


cases = [
    [2, 1, 5],
    [2, 7, 4, 3, 5],
    [1, 7, 5, 1, 9, 2, 5, 1],
]

for c in cases:
    s = Solution().nextLargerNodes(c)
