'''
1. find three subsets of first player's node -> parent / left / right
2. calculate number of nodes in each subset and compare
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.val)


class Solution:
    def btreeGameWinningMove(self, root, n, x):
        counts = [0, 0]

        def count(node):
            if not node:
                return 0
            left_sub, right_sub = count(node.left), count(node.right)
            if node.val == x:
                counts[0], counts[1] = left_sub, right_sub
            return left_sub + right_sub + 1
        return count(root) / 2 < max(max(counts), n-sum(counts)-1)

    def find_node_by_value(self, value, root):
        if root is None:
            return root
        if root.val == value:
            return root
        left = self.find_node_by_value(value, root.left)
        if left:
            return left
        else:
            return self.find_node_by_value(value, root.right)

    def count_subset(self, node):
        if node is None:
            return 0
        return 1 + self.count_subset(node.left) + self.count_subset(node.right)

    def btreeGameWinningMove2(self, root: TreeNode, n, x):
        node_x = self.find_node_by_value(x, root)      # O(n) for searching BST
        left_count = self.count_subset(node_x.left)    # O(n)
        right_count = self.count_subset(node_x.right)  # O(n)

        parent_count = n - (left_count + right_count + 1)

        return any([parent_count > left_count + right_count,
                    left_count > parent_count + right_count,
                    right_count > parent_count + left_count])


treelist = [TreeNode(x) for x in range(1, 12)]

treelist[0].left = treelist[1]
treelist[0].right = treelist[2]
treelist[1].left = treelist[3]
treelist[1].right = treelist[4]
treelist[2].left = treelist[5]
treelist[2].right = treelist[6]
treelist[3].left = treelist[7]
treelist[3].right = treelist[8]
treelist[4].left = treelist[9]
treelist[4].right = treelist[10]

s = Solution().btreeGameWinningMove(treelist[0], 11, 3)
print(s)
