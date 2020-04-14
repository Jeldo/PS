# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def showNodes(head: TreeNode):
    def dfs(head: TreeNode):
        if head:
            print(head.val, end=' ')
            dfs(head.left)
            dfs(head.right)
    dfs(head)
    print()


class Solution:
    def delNodes(self, root: TreeNode, to_delete: list):
        to_delete = set(to_delete)
        parents = list()

        def deleteNum(root: TreeNode):
            nonlocal to_delete

            if not root:
                return
            if root.val in to_delete:
                root.val = None
            deleteNum(root.left)
            deleteNum(root.right)

        def add_parent(root: TreeNode):
            nonlocal to_delete
            nonlocal parents

            if not root:
                return
            if root.val == None:
                if root.left and root.left.val:
                    parents.append(root.left)
                if root.right and root.right.val:
                    parents.append(root.right)
            add_parent(root.left)
            add_parent(root.right)
            if root.left and root.left.val == None:
                root.left = None
            if root.right and root.right.val == None:
                root.right = None

        deleteNum(root)
        if root.val:
            parents.append(root)
        add_parent(root)
        for p in parents:
            showNodes(p)
        return parents


cases = list()

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
dels = [1]
cases.append([head, dels])

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
dels = [3]
cases.append([head, dels])

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)
dels = [2]
cases.append([head, dels])

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)
head.right.left = TreeNode(6)
head.right.right = TreeNode(7)
dels = [3, 5]
cases.append([head, dels])


for c in cases:
    s = Solution().delNodes(c[0], c[1])
    print(s)
