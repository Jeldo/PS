# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level = 1
        maximal = float('-inf')
        q = deque([(root, 1)])
        while q:
            level_sum = 0
            for _ in range(len(q)):
                node, lvl = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append((node.left, lvl + 1))
                if node.right:
                    q.append((node.right, lvl + 1))
            if maximal < level_sum:
                maximal = level_sum
                level = lvl

        return level
