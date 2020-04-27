'''
Category: BFS, Tree
'''

from collections import defaultdict


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root, target, K):
        conn = defaultdict(list)

        def connect(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left:
                connect(child, child.left)
            if child.right:
                connect(child, child.right)

        connect(None, root)
        print(conn)
        bfs = [target.val]
        seen = set(bfs)
        for i in range(K):
            print(seen)
            new_level = []
            for q_node_val in bfs:
                for connected_node_val in conn[q_node_val]:
                    if connected_node_val not in seen:
                        new_level.append(connected_node_val)
            bfs = new_level
            seen |= set(bfs)
        return bfs


cases = list()

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
cases.append([head, head.right, 1])

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
cases.append([head, head.right, 2])

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)
cases.append([head, head.right, 2])

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)
head.right.left = TreeNode(8)
head.right.right = TreeNode(7)
cases.append([head, head.left.left, 3])

head = TreeNode(3)
head.left = TreeNode(9)
head.right = TreeNode(20)
head.right.left = TreeNode(15)
head.right.right = TreeNode(7)
cases.append([head, head.right.left, 3])

for c in cases:
    print(c)
    s = Solution().distanceK(c[0], c[1], c[2])
    print(s)
