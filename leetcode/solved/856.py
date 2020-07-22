'''
Category: String
Time Complexity: O(S)
'''


class Solution:
    def scoreOfParentheses(self, S):
        score = 0
        depth = 0
        prev = ''
        cur = ''
        for p in S:
            cur = p
            if p == '(':
                depth += 1
            else:
                depth -= 1
                if prev == '(':
                    score += 2**depth
            prev = p
        return score

    def scoreOfParentheses2(self, S):
        score = 0
        prev = ''
        level = 0
        for p in S:
            if p == '(':
                level += 1
            else:
                level -= 1
                if prev == '(':
                    score += 2 ** level
            prev = p
        return score


cases = [
    '()',
    '(())',
    '()()',
    '(()(()))',
    '(()(()(())))'
]

for c in cases:
    s = Solution().scoreOfParentheses(c)
    print(s)
