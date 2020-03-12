# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumEvenGrandparent(self, root: TreeNode):
        count = 0

        def dfs(node: TreeNode):
            nonlocal count
            if node.left:
                if node.val % 2 == 0:
                    if node.left.left:
                        count += node.left.left.val
                    if node.left.right:
                        count += node.left.right.val
                dfs(node.left)
            if node.right:
                if node.val % 2 == 0:
                    if node.right.left:
                        count += node.right.left.val
                    if node.right.right:
                        count += node.right.right.val
                dfs(node.right)
        dfs(root)
        return count


# root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
root = TreeNode(6)
a = TreeNode(7)
b = TreeNode(8)
c = TreeNode(2)
d = TreeNode(7)
e = TreeNode(1)
f = TreeNode(3)
g = TreeNode(9)
h = TreeNode(1)
i = TreeNode(4)
j = TreeNode(5)
root.left = a
root.right = b
a.left = c
a.right = d
b.left = e
b.right = f
c.left = g
d.left = h
d.right = i
f.right = j

s = Solution().sumEvenGrandparent(root)
print(s)
