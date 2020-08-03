'''
Category: DFS
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumEvenGrandparent(self, root: TreeNode):
        count = 0

        def dfs(node: TreeNode):
            nonlocal count
            if node.left:
                if node.val % 2 == 0:
                    if node.left.left:
                        count += node.left.left.val
                    if node.left.right:
                        count += node.left.right.val
                dfs(node.left)
            if node.right:
                if node.val % 2 == 0:
                    if node.right.left:
                        count += node.right.left.val
                    if node.right.right:
                        count += node.right.right.val
                dfs(node.right)
        dfs(root)
        return count

    def sumEvenGrandparent2(self, root: TreeNode):
        total = 0

        def dfs(node: TreeNode, p: TreeNode, gp: TreeNode):
            nonlocal total
            if not node:
                return
            if gp and gp.val % 2 == 0:
                total += node.val
            dfs(node.left, node, p)
            dfs(node.right, node, p)
        dfs(root, None, None)
        return total


cases = []

root = TreeNode(6)
root.left = TreeNode(7)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)
root.right.left = TreeNode(1)
root.right.right = TreeNode(3)
root.left.left.left = TreeNode(9)
root.left.right.left = TreeNode(1)
root.left.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
cases.append(root)

for c in cases:
    s = Solution().sumEvenGrandparent2(c)
    print(s)
