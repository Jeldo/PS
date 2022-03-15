class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        nodes = []

        def dfs(node: Optional[TreeNode]):
            nonlocal nodes
            if not node:
                return

            dfs(node.left)
            nodes.append(node)
            dfs(node.right)

        dfs(root)

        for i in range(len(nodes) - 1):
            if nodes[i].val >= nodes[i + 1].val:
                return False

        return True

    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], left_value, right_value):
            if not node:
                return True
            return (
                    left_value < node.val < right_value and
                    dfs(node.left, left_value, node.val) and
                    dfs(node.right, node.val, right_value)
            )

        return dfs(root, float('-inf'), float('inf'))
