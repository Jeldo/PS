class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        min_s = "z" * 8500

        def dfs(node, s):
            nonlocal min_s
            if not node:
                return
            s = chr(node.val + ord("a")) + s
            if not node.left and not node.right:
                min_s = min(min_s, s)
                return
            dfs(node.left, s)
            dfs(node.right, s)

        dfs(root, "")
        return min_s
