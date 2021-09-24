class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        right_side = defaultdict(int)
        q = deque([(root, 0)])
        while q:
            node, level = q.popleft()
            right_side[level] = node.val
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))

        return list(right_side.values())
