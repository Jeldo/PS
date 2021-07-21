import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def mergeKLists(self, lists: list[ListNode]) -> ListNode:
#         if not lists:
#             return ListNode()
#         for node in lists:
#             while node:
#                 print(node.val)
#                 node = node.next
#         return None


class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        pq = []
        for i, node in enumerate(lists):
            while node:
                heapq.heappush(pq, (node.val, i, node))
                node = node.next

        root = head = ListNode()
        while pq:
            _, _, node = heapq.heappop(pq)
            head.next = node
            head = head.next
        return root.next


cases = []

first = []
node = ListNode(1)
node.next = ListNode(4)
node.next.next = ListNode(5)
first.append(node)
node = ListNode(1)
node.next = ListNode(3)
node.next.next = ListNode(4)
first.append(node)
node = ListNode(2)
node.next = ListNode(6)
first.append(node)
cases.append(first)

for c in cases:
    res = Solution().mergeKLists(c)
    node = res
    while node:
        print(node.val)
        node = node.next
