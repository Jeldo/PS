"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# O(n)


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        q = deque()
        q.append((root, 1))
        prev_node = root
        prev_level = 0
        while q:
            node, level = q.popleft()
            if prev_level != level:
                prev_node.next = None
                prev_level = level
            else:
                prev_node.next = node
            prev_node = node
            if node.left:
                q.append((node.left, level+1))
            if node.right:
                q.append((node.right, level+1))

        return root
