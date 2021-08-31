# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        longest = 0

        def dfs(node, prev_value):
            nonlocal longest
            if not node:
                return 0
            left = dfs(node.left, node.val)
            right = dfs(node.right, node.val)
            longest = max(longest, left + right)
            if node.val == prev_value:
                return max(left, right) + 1
            return 0

        if not root:
            return 0

        dfs(root, root.val)
        return longest
