class Solution:
    def scoreOfParentheses(self, S):
        return


cases = [
    '()',
    '(())',
    '()()',
    '(()(()))'
]

for c in cases:
    s = Solution().queryString(c)
    print(s)
