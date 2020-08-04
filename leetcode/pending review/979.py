'''
Category: Tree, DFS
Time Complexity: 
Space Complexity: 
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distributeCoins(self, root: TreeNode):
        count = 0

        def dfs(node: TreeNode):
            nonlocal count
            if not node:
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            count += abs(left) + abs(right)
            return node.val + left + right - 1
        dfs(root)
        return count

    def distributeCoins2(self, root: TreeNode):
        count = 0
        cur = root

        def dfs(node: TreeNode):
            nonlocal count
            nonlocal cur
            if not node:
                return
            dfs(node.left)
            dfs(node.right)

            if node.left:
                while node.left.val > 1:
                    node.left.val -= 1
                    node.val += 1
                    count += 1
                while node.left.val < 1:
                    node.left.val += 1
                    node.val -= 1
                    count += 1
            if node.right:
                while node.right.val > 1:
                    node.right.val -= 1
                    node.val += 1
                    count += 1
                while node.right.val < 1:
                    node.right.val += 1
                    node.val -= 1
                    count += 1

        dfs(root)
        return count


cases = []

root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(0)
cases.append(root)

root = TreeNode(0)
root.left = TreeNode(3)
root.right = TreeNode(0)
cases.append(root)

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(2)
cases.append(root)

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(0)
root.left.right = TreeNode(3)
cases.append(root)

for c in cases:
    s = Solution().distributeCoins(c)
    print(s)
