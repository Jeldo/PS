# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.total = 0

    # dumbass
    def sumall(self, root):
        if root is None:
            return 0
        if root.left and not root.left.left and not root.left.right:
            self.total += root.left.val
        if root.left:
            self.sumall(root.left)
        if root.right:
            self.sumall(root.right)

    def sumOfLeftLeaves2(self, root):
        self.sumall(root)
        return self.total

    # recursion
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
