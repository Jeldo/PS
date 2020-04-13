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


def showNodes(head: TreeNode):
    if head:
        print(head.val, end=' ')
        showNodes(head.left)
        showNodes(head.right)


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

        # too slow
        def dfs2(node: TreeNode):
            nonlocal count
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            if node.left:
                if node.left.val > 1:
                    temp = node.left.val - 1
                    node.left.val -= temp
                    node.val += temp
                    count += temp
                if node.left.val < 1:
                    temp = -node.left.val + 1
                    node.left.val += temp
                    node.val -= temp
                    count += temp
            if node.right:
                if node.right.val > 1:
                    temp = node.right.val - 1
                    node.right.val -= temp
                    node.val += temp
                    count += temp
                if node.right.val < 1:
                    temp = -node.right.val + 1
                    node.right.val += temp
                    node.val -= temp
                    count += temp

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


head1 = TreeNode(3)
head1.left = TreeNode(0)
head1.right = TreeNode(0)

head2 = TreeNode(0)
head2.left = TreeNode(3)
head2.right = TreeNode(0)

head3 = TreeNode(1)
head3.left = TreeNode(0)
head3.right = TreeNode(2)

head4 = TreeNode(1)
head4.left = TreeNode(0)
head4.right = TreeNode(0)
head4.left.right = TreeNode(3)

head5 = TreeNode(4)
head5.left = TreeNode(0)
head5.left.right = TreeNode(0)
head5.left.right.right = TreeNode(0)

cases = [
    head1, head2, head3, head4, head5
]

for c in cases:
    s = Solution().distributeCoins(c)
    print(s)
