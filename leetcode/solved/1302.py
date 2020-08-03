'''
Category: DFS
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deepestLeavesSum(self, root: TreeNode):
        max_level = 0
        count = 0

        def dfs(node: TreeNode, level):
            nonlocal count
            nonlocal max_level
            if not node:
                return
            if max_level < level:
                max_level = level
                count = node.val
            elif max_level == level:
                count += node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        return count

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


cases = []

treelist = [TreeNode(x) for x in range(1, 9)]

treelist[0].left = treelist[1]      # 2
treelist[0].right = treelist[2]     # 3
treelist[1].left = treelist[3]      # 4
treelist[1].right = treelist[4]     # 5
treelist[3].left = treelist[6]      # 7
treelist[2].right = treelist[5]     # 6
treelist[5].right = treelist[7]     # 8
cases.append(treelist)

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
cases.append(treelist)

for c in cases:
    s = Solution().deepestLeavesSum(c[0])
    print(s)
