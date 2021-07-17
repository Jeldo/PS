class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head

            prev.next = b

            head = head.next
            prev = prev.next.next

        return root.next

    def swapPairs_recursively(self, head: ListNode) -> ListNode:
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        return head


cases = []
n = ListNode(1)
n.next = ListNode(2)
n.next.next = ListNode(3)
n.next.next.next = ListNode(4)
cases.append(n)
cases.append(None)
cases.append(ListNode(1))

for c in cases:
    res = Solution().swapPairs(c)
    while res:
        print(res.val)
        res = res.next
    print()
