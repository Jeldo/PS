# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class Solution:
    def kthSmallest(self, root: TreeNode, k: int):
        node_list = list()

        def search_tree(node):
            if node is not None:
                node_list.append(node.val)
                search_tree(node.left)
                search_tree(node.right)
        search_tree(root)
        node_list.sort()
        return node_list[k-1]


treelist = [TreeNode(x) for x in range(1, 7)]
root = treelist[4]
treelist[4].left = treelist[2]
treelist[4].right = treelist[5]
treelist[2].left = treelist[1]
treelist[2].right = treelist[3]
treelist[1].left = treelist[0]

s = Solution().kthSmallest(root, 3)
print(s)
