# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        carry = 0
        root = node = ListNode(0)

        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum + carry, 10)
            node.next = ListNode(val)
            node = node.next
        return root.next

    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = node = ListNode(val=0)
        carry = 0

        while l1 or l2:
            two_sum = 0
            if l1:
                two_sum += l1.val
            if l2:
                two_sum += l2.val
            two_sum += carry

            carry, remainder = divmod(two_sum, 10)
            node.next = ListNode(val=remainder)
            node = node.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        # handle last carry
        if carry == 1:
            node.next = ListNode(val=carry)

        return head.next


cases = []
ll1 = ListNode(2)
ll1.next = ListNode(4)
ll1.next.next = ListNode(3)
ll2 = ListNode(5)
ll2.next = ListNode(6)
ll2.next.next = ListNode(4)
cases.append([ll1, ll2])

ll1 = ListNode(0)
ll2 = ListNode(0)
cases.append([ll1, ll2])

ll1 = ListNode(9)
ll1.next = ListNode(9)
ll1.next.next = ListNode(9)
ll1.next.next.next = ListNode(9)
ll1.next.next.next.next = ListNode(9)
ll1.next.next.next.next.next = ListNode(9)
ll1.next.next.next.next.next.next = ListNode(9)
ll2 = ListNode(9)
ll2.next = ListNode(9)
ll2.next.next = ListNode(9)
ll2.next.next.next = ListNode(9)
cases.append([ll1, ll2])

for c in cases:
    res = Solution().addTwoNumbers(*c)
    print(res)
