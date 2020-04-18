'''
Category: Tree, DFS
Time Complexity: O(n)
Space Complexity: O(1)
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxAncestorDiff(self, root: TreeNode):
        max_diff = 0

        def dfs(node: TreeNode, max_val, min_val):
            nonlocal max_diff
            if not node:
                diff = max_val - min_val
                max_diff = max(max_diff, diff)
                return
            max_val = max(max_val, node.val)
            min_val = min(min_val, node.val)
            dfs(node.left, max_val, min_val)
            dfs(node.right, max_val, min_val)

        dfs(root, root.val, root.val)
        return max_diff

    # too much time, too many memories consuming
    def maxAncestorDiff2(self, root: TreeNode):
        nodes = list()
        max_diff = 0

        def dfs(node: TreeNode, nodes: list):
            nonlocal max_diff
            if not node:
                diff = max(nodes)-min(nodes)
                max_diff = max(max_diff, diff)
                return
            new_nodes = nodes + [node.val]
            dfs(node.left, new_nodes)
            dfs(node.right, new_nodes)
        dfs(root, nodes)
        return max_diff


cases = list()

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)

head = TreeNode(8)
head.left = TreeNode(3)
head.right = TreeNode(10)
head.left.left = TreeNode(1)
head.left.right = TreeNode(6)
head.left.right.left = TreeNode(4)
head.left.right.right = TreeNode(7)
head.right.right = TreeNode(14)
head.right.right.left = TreeNode(13)
cases.append(head)

for c in cases:
    s = Solution().maxAncestorDiff(c)
    print(s)
