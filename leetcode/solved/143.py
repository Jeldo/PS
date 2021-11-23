# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        q = deque()
        node = head
        first = cursor = ListNode()

        while node:
            q.append(node)
            node = node.next

        left_turn = True
        while q:
            if left_turn:
                cursor.next = q.popleft()
            else:
                cursor.next = q.pop()
            cursor = cursor.next
            left_turn = not left_turn

        cursor.next = None
        return first.next
