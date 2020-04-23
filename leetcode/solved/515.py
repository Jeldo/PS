'''
Category: BFS, Tree, DFS
'''

from queue import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def showNodes(head: TreeNode):
    def dfs(head: TreeNode):
        if head:
            print(head.val, end=' ')
            dfs(head.left)
            dfs(head.right)
    dfs(head)
    print()


class Solution:
    def largestValues(self, root: TreeNode):
        if not root:
            return []
        q = deque()
        q.append(root)
        max_values = list()

        while q:
            temp_q = deque()
            for node in q:
                if node.left:
                    temp_q.append(node.left)
                if node.right:
                    temp_q.append(node.right)
            max_value = max([x.val for x in q])
            max_values.append(max_value)
            q = temp_q
        return max_values


cases = list()

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
cases.append(head)

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
cases.append(head)

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)
cases.append(head)

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)
head.right.left = TreeNode(8)
head.right.right = TreeNode(7)
cases.append(head)

cases.append([])

for c in cases:
    s = Solution().largestValues2(c)
    print(s)
