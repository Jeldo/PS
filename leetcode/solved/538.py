# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        right_sum = 0

        def dfs(node: TreeNode):
            nonlocal right_sum

            if not node:
                return

            dfs(node.right)
            node.val += right_sum
            right_sum = node.val
            dfs(node.left)

        dfs(root)
        return root
