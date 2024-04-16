class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = None
        while head:
            temp = head.next
            head.next = tail
            tail = head
            head = temp
        return tail
