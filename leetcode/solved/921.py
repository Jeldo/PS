class Solution:
    def minAddToMakeValid(self, S):
        stack = []
        n = 0
        for p in S:
            if len(stack) == 0:
                stack.append(p)
            elif stack[-1] == '(' and p == ')':
                stack.pop()
                n += 1
            else:
                stack.append(p)
        return len(stack)

    def minAddToMakeValid2(self, S):
        left = right = 0
        for p in S:
            if right == 0 and p == ')':
                left += 1
            else:
                if p == '(':
                    right += 1
                else:
                    right -= 1
        return left + right


cases = [
    '())',
    '(((',
    '()',
    '()))((',
    '((())'
]

for c in cases:
    s = Solution().minAddToMakeValid2(c)
    print(s)
