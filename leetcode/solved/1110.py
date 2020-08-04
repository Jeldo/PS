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
            heads = []
            to_delete = set(to_delete)

        def remove_val(node: TreeNode):
            if not node:
                return
            if node.val in to_delete:
                to_delete.remove(node.val)
                node.val = None
            remove_val(node.left)
            remove_val(node.right)

        def find_head(node: TreeNode, prev_val):
            nonlocal heads
            if not node:
                return
            if node.val and not prev_val:
                heads.append(node)
            find_head(node.left, node.val)
            find_head(node.right, node.val)

        def remove_node(node: TreeNode):
            if not node:
                return
            remove_node(node.left)
            remove_node(node.right)
            if node.left and not node.left.val:
                node.left = None
            if node.right and not node.right.val:
                node.right = None

        remove_val(root)
        find_head(root, None)
        remove_node(root)
        return heads

    def delNodes2(self, root: TreeNode, to_delete: list):
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


cases = []

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
cases.append([root, [3, 5]])

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
cases.append([root, [3, 5, 6]])

for c in cases:
    s = Solution().delNodes(c[0], c[1])
    print(s)
