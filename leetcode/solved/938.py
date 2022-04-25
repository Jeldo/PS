class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        total = 0

        def dfs(node):
            nonlocal total
            if not node:
                return

            if low <= node.val <= high:
                total += node.val
            if low <= node.val:
                dfs(node.left)
            if node.val <= high:
                dfs(node.right)

        dfs(root)
        return total
