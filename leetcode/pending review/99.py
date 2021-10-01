# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional


# inorder traversal
# current node's value should be bigger than prev's value
# otherwise, it does not comply with the property of BST.

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        first, second, prev = None, None, TreeNode(float('-inf'))

        def dfs(node: TreeNode):
            nonlocal first, second, prev
            if not node:
                return

            dfs(node.left)
            if node.val < prev.val:
                if not first:
                    first = prev
                second = node
            prev = node
            dfs(node.right)

        dfs(root)
        first.val, second.val = second.val, first.val
