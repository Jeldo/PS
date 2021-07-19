# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        i = 1
        odd_head = odd_node = ListNode()
        even_head = even_node = ListNode()
        while head:
            if i % 2 != 0:
                odd_node.next = head
                odd_node = odd_node.next
            else:
                even_node.next = head
                even_node = even_node.next
            i += 1
            head = head.next

        even_node.next = None
        odd_node.next = even_head.next
        return odd_head.next


cases = []
# 1 3 5 2 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
cases.append(head)

# 2 3 6 7 1 5 4
head = ListNode(2)
head.next = ListNode(1)
head.next.next = ListNode(3)
head.next.next.next = ListNode(5)
head.next.next.next.next = ListNode(6)
head.next.next.next.next.next = ListNode(4)
head.next.next.next.next.next.next = ListNode(7)
cases.append(head)

for c in cases:
    res = Solution().oddEvenList(c)
    node = res
    while node:
        print(node.val)
        node = node.next
    print()
