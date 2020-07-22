'''
Category: Stack
Time Complexity: O(n)
'''


class Solution:
    def reverseParentheses(self, s):
        return ''


cases = [
    "(abcd)",
    "(u(love)i)",
    "(ed(et(oc))el)",
    "a(bcdefghijkl(mno)p)q"
]

for c in cases:
    s = Solution().reverseParentheses(c)
    print(s)
