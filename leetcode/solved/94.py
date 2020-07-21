'''
Category: Stack
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: TreeNode):
        answer = []

        def dfs(node: TreeNode):
            nonlocal answer
            if not node:
                return
            dfs(node.left)
            answer.append(node.val)
            dfs(node.right)
        dfs(root)
        return answer


cases = []

head = TreeNode(1)
head.right = TreeNode(2)
head.right.left = TreeNode(3)
cases.append(head)

for c in cases:
    s = Solution().inorderTraversal(c)
    print(s)
