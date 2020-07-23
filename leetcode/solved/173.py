'''
Category: Stack, Tree, Design
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.i = 0
        self.values = []

        def dfs(node: TreeNode):
            if not node:
                return
            dfs(node.left)
            self.values.append(node.val)
            dfs(node.right)
        dfs(root)

    def next(self):
        self.i += 1
        return self.values[self.i - 1]

    def hasNext(self):
        if self.i < len(self.values):
            return True
        else:
            return False
