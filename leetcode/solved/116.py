class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return

        prev = Node()
        level = 0
        q = deque([(root, 0)])
        while q:
            node, lvl = q.popleft()
            if lvl != level:
                prev.next = None
                level += 1
            else:
                prev.next = node
            prev = node
            if node.left:
                q.append((node.left, lvl + 1))
            if node.right:
                q.append((node.right, lvl + 1))

        return root