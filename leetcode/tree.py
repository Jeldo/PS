class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder_traversal(node: TreeNode):
    if node is None:
        return
    print(node.val)
    inorder_traversal(node.left)
    inorder_traversal(node.right)


def preorder_traversal(node: TreeNode):
    if node is None:
        return
    preorder_traversal(node.left)
    print(node.val)
    preorder_traversal(node.right)


def postorder_traversal(node: TreeNode):
    if node is None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.val)


cases = []

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
root.left.left.left = TreeNode(8)
root.left.left.right = TreeNode(9)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(11)
root.right.left.left = TreeNode(12)
root.right.left.right = TreeNode(13)
root.right.right.left = TreeNode(14)
root.right.right.right = TreeNode(15)
cases.append(root)

inorder_traversal(root)
print('=============')
preorder_traversal(root)
print('=============')
postorder_traversal(root)
