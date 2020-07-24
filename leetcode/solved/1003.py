'''
Category: Stack, Linked List
'''


class Solution:
    def isValid(self, S: str):
        stack = []
        for ch in S:
            stack.append(ch)
            if len(stack) > 2 and stack[-1] == 'c' and stack[-2] == 'b' and stack[-3] == 'a':
                for _ in range(3):
                    stack.pop()
        return len(stack) == 0

    def isValid2(self, S):
        stack = []
        for i in S:
            if i == 'c':
                if stack[-2:] != ['a', 'b']:
                    return False
                stack.pop()
                stack.pop()
            else:
                stack.append(i)
        return not stack


cases = [
    "aabcbc",
    "abcabcababcc",
    "abccba",
    "cababc"
]

for c in cases:
    s = Solution().isValid(c)
    print(s)
