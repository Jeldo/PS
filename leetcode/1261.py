'''
Category: Hash Table
'''


class FindElements:
    def __init__(self, root: TreeNode):
        self.s = set()
        root.val = 0

        def dfs(node: TreeNode):
            if node.left:
                recovery = node.val * 2 + 1
                node.left.val = recovery
                if recovery not in self.s:
                    self.s.add(recovery)
                dfs(node.left)
            if node.right:
                recovery = node.val * 2 + 2
                node.right.val = recovery
                if recovery not in self.s:
                    self.s.add(recovery)
                dfs(node.right)
        dfs(root)

    def find(self, target: int):
        return target in self.s


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
