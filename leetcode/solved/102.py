'''
Category: BFS, Tree
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
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        levelOrderValues = list()
        q = list()
        q.append(root)
        while q:
            levelOrderValues.append([x.val for x in q])
            temp_q = list()
            for node in q:
                if node.left:
                    temp_q.append(node.left)
                if node.right:
                    temp_q.append(node.right)
            q = temp_q
        return levelOrderValues


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

head = TreeNode(3)
head.left = TreeNode(9)
head.right = TreeNode(20)
head.right.left = TreeNode(15)
head.right.right = TreeNode(7)
cases.append(head)

for c in cases:
    s = Solution().levelOrder(c)
    print(s)
