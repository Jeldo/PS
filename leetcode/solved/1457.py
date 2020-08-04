'''
Category: DFS, Tree, Bit-manipulation
'''
from collections import Counter


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pseudoPalindromicPaths(self, root: TreeNode):
        count = 0

        def dfs(node: TreeNode, val_list: list):
            nonlocal count
            if node.left:
                dfs(node.left, val_list + [node.val])
            if node.right:
                dfs(node.right, val_list + [node.val])
            if not node.left and not node.right:
                nums = val_list + [node.val]
                odd_counter = 0
                for v in Counter(nums).values():
                    if v % 2 != 0:
                        odd_counter += 1
                if odd_counter <= 1:
                    count += 1
                return
        dfs(root, [])
        return count


cases = []

root = TreeNode(2)
root.left = TreeNode(3)
root.right = TreeNode(1)
root.left.left = TreeNode(3)
root.left.right = TreeNode(1)
root.right.right = TreeNode(1)
cases.append(root)


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(1)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.left.right.right = TreeNode(1)
cases.append(root)

for c in cases:
    s = Solution().pseudoPalindromicPaths2(c)
    print(s)
