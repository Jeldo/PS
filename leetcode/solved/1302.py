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

    # dumb
    def deepestLeavesSum(self, TreeNode):
        total = 0
        q = list()
        new_q = list()
        q.append(TreeNode)
        while q:
            cur_node = q.pop(0)
            if not cur_node.left and not cur_node.right and not new_q:
                total += cur_node.val
            if cur_node.left:
                new_q.append(cur_node.left)
                total = 0
            if cur_node.right:
                new_q.append(cur_node.right)
                total = 0
            if not q:
                q = new_q.copy()
                new_q.clear()
        return total

    # BFS
    def deepestLeavesSum2(self, root):
        if not root:
            return 0
        q = [root]
        total = 0
        while q:
            for _ in range(len(q)):
                node = q.pop(0)
                total += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if q:
                total = 0
        return total


# treelist = [TreeNode(x) for x in range(1,9)]

# treelist[0].left = treelist[1]      # 2
# treelist[0].right = treelist[2]     # 3
# treelist[1].left = treelist[3]      # 4
# treelist[1].right = treelist[4]     # 5
# treelist[3].left = treelist[6]      # 7
# treelist[2].right = treelist[5]     # 6
# treelist[5].right = treelist[7]     # 8

nums = [38, 43, 70, 16, 78, 91, 71, 27, 71, 71]
treelist = [TreeNode(x) for x in nums]

treelist[0].left = treelist[1]
treelist[0].right = treelist[2]
treelist[1].left = treelist[3]
treelist[2].left = treelist[4]
treelist[2].right = treelist[5]
treelist[3].right = treelist[6]
treelist[4].left = treelist[7]
treelist[5].left = treelist[8]
treelist[7].right = treelist[9]

s = Solution().deepestLeavesSum(treelist[0])
print('answer:', s)
