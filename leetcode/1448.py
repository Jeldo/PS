'''
Category: DFS, Tree
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode):
        count = 0

        def dfs(node: TreeNode, prev_max):
            nonlocal count
            if not node:
                return
            if node.val >= prev_max:
                prev_max = node.val
                count += 1
            dfs(node.left, prev_max)
            dfs(node.right, prev_max)
        dfs(root, -10**5)
        return count


cases = []

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.left = TreeNode(3)
# root.left.right = TreeNode(7)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)
# root.left.left.left = TreeNode(9)
# root.left.left.right = TreeNode(10)
# root.left.right.left = TreeNode(1)
# root.left.right.right = TreeNode(4)
# root.right.right.left = TreeNode(3)
# root.right.right.right = TreeNode(5)
cases.append(root)

root = TreeNode(3)
root.left = TreeNode(3)
# root.right = TreeNode(4)
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
# root.right.left = TreeNode(1)
# root.right.right = TreeNode(5)
# root.left.left.left = TreeNode(9)
# root.left.left.right = TreeNode(10)
# root.left.right.left = TreeNode(1)
# root.left.right.right = TreeNode(4)
# root.right.right.left = TreeNode(3)
# root.right.right.right = TreeNode(5)
cases.append(root)

root = TreeNode(1)
# root.left = TreeNode(3)
# root.right = TreeNode(4)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(2)
# root.right.left = TreeNode(1)
# root.right.right = TreeNode(5)
# root.left.left.left = TreeNode(9)
# root.left.left.right = TreeNode(10)
# root.left.right.left = TreeNode(1)
# root.left.right.right = TreeNode(4)
# root.right.right.left = TreeNode(3)
# root.right.right.right = TreeNode(5)
cases.append(root)

for c in cases:
    s = Solution().goodNodes(c)
    print(s)
