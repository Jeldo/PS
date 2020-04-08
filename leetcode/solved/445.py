'''
Category: Linked List
Time Complexity: O(max(l1, l2))
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        list1, list2 = list(), list()
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next
        if len(list1) < len(list2):
            list1 = [0] * (len(list2)-len(list1)) + list1
        elif len(list1) > len(list2):
            list2 = [0] * (len(list1)-len(list2)) + list2
        ans = list()
        carry = 0
        for x in reversed(range(len(list1))):
            num = list1[x] + list2[x] + carry
            carry = 0
            if num >= 10:
                num -= 10
                carry = 1
            ans.insert(0, num)
        if carry == 1:
            ans.insert(0, 1)
        node = ListNode(ans[0])
        head = node
        for i in range(1, len(ans)):
            node.next = ListNode(ans[i])
            node = node.next
        return head

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode):
        list1, list2 = list(), list()
        while l1:
            list1.append(str(l1.val))
            l1 = l1.next
        while l2:
            list2.append(str(l2.val))
            l2 = l2.next
        number = int(''.join(list1)) + int(''.join(list2))
        nums = list()
        while True:
            nums.insert(0, number % 10)
            number = number // 10
            if number == 0:
                break
        node = ListNode(nums[0])
        head = node
        for i in range(1, len(nums)):
            node.next = ListNode(nums[i])
            node = node.next
        return head


a = ListNode(7)
b = ListNode(2)
c = ListNode(4)
d = ListNode(3)
a.next = b
b.next = c
c.next = d


aa = ListNode(5)
bb = ListNode(6)
cc = ListNode(4)
aa.next = bb
bb.next = cc

z = ListNode(0)
zz = ListNode(0)

e = ListNode(5)
ee = ListNode(5)

cases = [
    [a, aa],
    [z, zz],
    [e, ee]
]

for case in cases:
    s = Solution().addTwoNumbers(case[0], case[1])
    print(s)
