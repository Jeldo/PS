class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        q = deque([(root, root.val)])
        while q:
            node, num = q.popleft()
            if not node.left and not node.right:
                total += num
            if node.left:
                q.append((node.left, num * 10 + node.left.val))
            if node.right:
                q.append((node.right, num * 10 + node.right.val))
        return total
