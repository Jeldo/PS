class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced = True

        def dfs(node):
            nonlocal is_balanced
            if not node:
                return 0

            left_level = dfs(node.left)
            right_level = dfs(node.right)
            if abs(left_level - right_level) > 1:
                is_balanced = False

            return max(left_level, right_level) + 1

        dfs(root)
        return is_balanced
