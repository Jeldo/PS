'''
Category: Linked List
Time Complexity: O(n)
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head: ListNode):
        binary = list()
        ans = 0
        node = head
        while node:
            binary.append(node.val)
            node = node.next

        for i, n in enumerate(binary):
            ans += n*2**(len(binary) - 1 - i)
        return ans


a = ListNode(1)
b = ListNode(0)
c = ListNode(1)

a.next = b
b.next = c

s = Solution().getDecimalValue(a)
print(s)
