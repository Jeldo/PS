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

    def longestUnivaluePath2(self, root: Optional[TreeNode]) -> int:
        longest_path = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal longest_path
            if not node:
                return 0

            left = dfs(node=node.left)
            right = dfs(node=node.right)

            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0

            longest_path = max(longest_path, left + right)
            return max(left, right)

        dfs(node=root)
        return longest_path
