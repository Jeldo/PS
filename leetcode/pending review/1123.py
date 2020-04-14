'''
Category: DFS, Tree
Solved, but need to review LCA
'''


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
    def lcaDeepestLeaves(self, root: TreeNode):
        def count_depth(root: TreeNode):
            if not root:
                return 0
            return 1 + max(count_depth(root.left), count_depth(root.right))

        if not root:
            return None
        left = count_depth(root.left)
        right = count_depth(root.right)
        if left == right:
            return root
        elif left < right:
            return self.lcaDeepestLeaves(root.right)
        else:
            return self.lcaDeepestLeaves(root.left)

    def lcaDeepestLeaves1(self, root: TreeNode):
        value_of_deepest_nodes = set()
        parents = list()
        matching_nodes = 0
        max_depth = 0

        def find_deepest_node(root: TreeNode, depth):
            nonlocal value_of_deepest_nodes
            nonlocal max_depth
            if not root:
                return
            if max_depth < depth:
                max_depth = depth
                value_of_deepest_nodes.clear()
                value_of_deepest_nodes.add(root.val)
            elif max_depth == depth:
                value_of_deepest_nodes.add(root.val)

            find_deepest_node(root.left, depth + 1)
            find_deepest_node(root.right, depth + 1)

        def count_found_node(root: TreeNode, matching_nodes):
            nonlocal value_of_deepest_nodes
            nonlocal parents
            if not root:
                return 0
            matching_nodes += count_found_node(root.left, matching_nodes) + \
                count_found_node(root.right, matching_nodes)
            if root.val in value_of_deepest_nodes:
                matching_nodes += 1
            if matching_nodes == len(value_of_deepest_nodes):
                parents.append(root)
            return matching_nodes

        find_deepest_node(root, 0)
        count_found_node(root, matching_nodes)
        return parents[0]


cases = list()

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
cases.append(head)

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
cases.append(head)

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)
cases.append(head)

head = TreeNode(1)
head.left = TreeNode(2)
head.right = TreeNode(3)
head.left.left = TreeNode(4)
head.left.right = TreeNode(5)
head.right.left = TreeNode(6)
head.right.right = TreeNode(7)
cases.append(head)


for c in cases:
    s = Solution().lcaDeepestLeaves(c)
    print(s)
