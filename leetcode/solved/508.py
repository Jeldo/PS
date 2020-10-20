'''
Category: Hash Table
'''
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: TreeNode):
        d = defaultdict(int)

        def dfs(node: TreeNode):
            nonlocal d
            if not node:
                return 0
            total = node.val + dfs(node.left) + dfs(node.right)
            d[total] += 1
            return total
        dfs(root)
        max_keys = []
        max_freq = 0
        print(d)
        for k, f in d.items():
            if max_freq < f:
                max_keys = [k]
                max_freq = f
            elif max_freq == f:
                max_keys.append(k)
        return max_keys


cases = []

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-3)
cases.append(root)

root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(-5)
cases.append(root)

for c in cases:
    s = Solution().findFrequentTreeSum(c)
    print(s)
