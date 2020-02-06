# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def recoverFromPreorder(self, S):


nums = [38, 43, 70, 16, 78, 91, 71, 27, 71, 71]
treelist = [TreeNode(x) for x in nums]

treelist[0].left = treelist[1]
treelist[0].right = treelist[2]
treelist[1].left = treelist[3]
treelist[2].left = treelist[4]
treelist[2].right = treelist[5]
treelist[3].right = treelist[6]
treelist[4].left = treelist[7]
treelist[5].left = treelist[8]
treelist[7].right = treelist[9]

SS = ''
s = Solution().recoverFromPreorder(SS)
