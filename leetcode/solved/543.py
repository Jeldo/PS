class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(node: Optional[TreeNode]) -> int:
            nonlocal diameter
            if not node:
                return 0

            left = dfs(node=node.left)
            right = dfs(node=node.right)
            diameter = max(diameter, left + right)
            return max(left, right) + 1

        dfs(node=root)
        return diameter
