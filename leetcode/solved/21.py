# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        head = node = ListNode(val=0)
        while list1 and list2:
            if list1.val <= list2.val:
                node.next = ListNode(val=list1.val)
                list1 = list1.next
            else:
                node.next = ListNode(val=list2.val)
                list2 = list2.next
            node = node.next

        if list1:
            node.next = list1
        if list2:
            node.next = list2

        return head.next
