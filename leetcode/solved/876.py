class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode):
        total = 0
        node = head
        while node:
            total += 1
            node = node.next
        node = head
        for i in range(total//2):
            node = node.next
        return node

    def middleNode2(self, head):
        mid = head
        count = 0
        while(head):
            if(count % 2):
                mid = mid.next
            count += 1
            head = head.next
        return mid


a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)

a.next = b
b.next = c
c.next = d
d.next = e

s = Solution().middleNode2(a)
print(s)
