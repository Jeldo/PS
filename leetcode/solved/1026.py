'''
Category: Tree, DFS
Time Complexity: O(n)
Space Complexity: O(1)
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode):
        max_diff = 0

        def dfs(node: TreeNode, max_val, min_val):
            nonlocal max_diff
            if not node:
                return
            max_val = max(max_val, node.val)
            min_val = min(min_val, node.val)
            max_diff = max(max_diff, abs(max_val - min_val))
            dfs(node.left, max_val, min_val)
            dfs(node.right, max_val, min_val)
        dfs(root, root.val, root.val)
        return max_diff


cases = []

root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.right.right = TreeNode(14)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right.left = TreeNode(13)
cases.append(root)

for c in cases:
    s = Solution().maxAncestorDiff(c)
    print(s)
