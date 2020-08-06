'''
Category: DFS, Tree
Time Complexity: O(n)
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode):
        left_most, deepest_level = root.val, 0

        def dfs(node: TreeNode, level):
            nonlocal left_most, deepest_level
            if not node:
                return
            if deepest_level < level:
                left_most = node.val
                deepest_level = level
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        return left_most

    # bfs
    def findBottomLeftValue2(self, root: TreeNode):
        max_level = 0
        deepest_value = root.val
        q = Queue()
        q.put((root, 0))

        while not q.empty():
            cur, level = q.get()
            if max_level < level:
                max_level = level
                deepest_value = cur.val
            left, right = cur.left, cur.right
            if left:
                q.put((left, level + 1))
            if right:
                q.put((right, level + 1))
        return deepest_value

    # bfs
    def findBottomLeftValue3(self, root: TreeNode):
        deepest_value = root.val
        q = deque()
        q.append(root)

        while q:
            deepest_value = q[0].val
            temp_q = deque()
            for node in q:
                if node.left:
                    temp_q.append(node.left)
                if node.right:
                    temp_q.append(node.right)
            q = temp_q
        return deepest_value


cases = []

root = TreeNode(1)
cases.append(root)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
cases.append(root)

root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
root.left.left = TreeNode(5)
root.right.right = TreeNode(4)
cases.append(root)

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)
cases.append(root)

for c in cases:
    s = Solution().findBottomLeftValue(c)
    print(s)
