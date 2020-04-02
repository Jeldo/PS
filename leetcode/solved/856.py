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
                if prev == '(' and cur == ')':
                    if depth == 0:
                        score += 1
                    else:
                        score += 2**(depth)
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
