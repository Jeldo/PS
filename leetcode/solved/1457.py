from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# O(n)


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        def dfs(node, palindrom_pairs):
            if not node:
                return 0
            if node.val in palindrom_pairs:
                palindrom_pairs.remove(node.val)
            else:
                palindrom_pairs.add(node.val)
            if not node.left and not node.right:
                return 1 if len(palindrom_pairs) <= 1 else 0
            return dfs(node.left, set(palindrom_pairs)) + dfs(node.right, set(palindrom_pairs))

        return dfs(root, set())
