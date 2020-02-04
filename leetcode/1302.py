# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max_level = 0
        self.total = 0

    def deepestLeavesSum(self, TreeNode, level):

        if not TreeNode:
            return 0
        # print(TreeNode.val, level, self.max_level, self.total)
        if level == self.max_level and not TreeNode.left and not TreeNode.right:
            self.total += TreeNode.val
        if level > self.max_level and not TreeNode.left and not TreeNode.right:
            self.total = TreeNode.val
            self.max_level = level
        else:
            self.deepestLeavesSum(TreeNode.left, level + 1)
            self.deepestLeavesSum(TreeNode.right, level + 1)
        return self.total


treelist = [TreeNode(x) for x in range(1, 9)]

treelist[0].left = treelist[1]      # 2
treelist[0].right = treelist[2]     # 3
treelist[1].left = treelist[3]      # 4
treelist[1].right = treelist[4]     # 5
treelist[3].left = treelist[6]      # 7
treelist[2].right = treelist[5]     # 6
treelist[5].right = treelist[7]     # 8

s = Solution().deepestLeavesSum(treelist[0], 0)
print(s)
