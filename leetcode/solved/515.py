'''
Category: DFS, Tree
Time Complexity: O(n)
'''


from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: TreeNode):
        d = dict()

        def dfs(node: TreeNode, level):
            if not node:
                return
            if not level in d:
                d[level] = node.val
            else:
                d[level] = max(d[level], node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        return [v for v in d.values()]

    # BFS
    def largestValues2(self, root: TreeNode):
        if not root:
            return []
        q = list()
        q.append(root)
        max_values = list()

        while q:
            temp_q = list()
            for node in q:
                if node.left:
                    temp_q.append(node.left)
                if node.right:
                    temp_q.append(node.right)
            max_value = max([x.val for x in q])
            max_values.append(max_value)
            q = temp_q
        return max_values


cases = []

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(9)
cases.append(root)

root = TreeNode(0)
root.left = TreeNode(-1)
cases.append(root)

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(4)
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(1)
root.right.right = TreeNode(5)
root.left.left.right = TreeNode(10)
root.left.right.right = TreeNode(4)
root.right.right.left = TreeNode(3)
root.right.right.right = TreeNode(5)
cases.append(root)

for c in cases:
    s = Solution().largestValues(c)
    print(s)
