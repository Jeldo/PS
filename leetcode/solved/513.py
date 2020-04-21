'''
Category: BFS, DFS, Tree
Time Complexity: O(n)
Space Complexity: 
'''
from queue import Queue
from queue import deque


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
    # inorder DFS
    def findBottomLeftValue(self, root: TreeNode):
        max_level = 0
        deepest_value = root.val

        def dfs(node: TreeNode, level):
            nonlocal max_level
            nonlocal deepest_value
            if not node:
                return
            if max_level < level:
                max_level = level
                deepest_value = node.val
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)

        dfs(root, 0)
        return deepest_value

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


cases = list()

head = TreeNode(2)
head.left = TreeNode(1)
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
head.right.left = TreeNode(5)
head.right.right = TreeNode(6)
head.right.left.left = TreeNode(7)
cases.append(head)

# head = TreeNode(8)
# head.left = TreeNode(3)
# head.right = TreeNode(10)
# head.left.left = TreeNode(1)
# head.left.right = TreeNode(6)
# head.left.right.left = TreeNode(4)
# head.left.right.right = TreeNode(7)
# head.right.right = TreeNode(14)
# head.right.right.left = TreeNode(13)
# cases.append(head)

for c in cases:
    s = Solution().findBottomLeftValue3(c)
    print('res:', s)
