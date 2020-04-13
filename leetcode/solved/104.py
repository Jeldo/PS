'''
Category: DFS, Tree
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode):
        count = 0

        def dfs(node: TreeNode, level):
            nonlocal count
            if not node:
                return
            count = max(count, level)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 1)
        return count


head = TreeNode(3)
head.left = TreeNode(9)
head.left.left = TreeNode(10)
head.left.left.left = TreeNode(10)
head.right = TreeNode(20)
head.right.left = TreeNode(15)
head.right.right = TreeNode(7)

cases = [
    head
]

for c in cases:
    s = Solution().maxDepth(c)
    print(s)
