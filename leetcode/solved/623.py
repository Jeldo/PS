class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val=val, left=root)
        q = deque([(root, 1)])
        while q:
            node, level = q.popleft()
            if level + 1 == depth:
                node.left = TreeNode(val=val, left=node.left)
                node.right = TreeNode(val=val, right=node.right)
                continue
            if node.left:
                q.append((node.left, level + 1))
            if node.right:
                q.append((node.right, level + 1))
        return root
