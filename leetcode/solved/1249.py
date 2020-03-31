class Solution:
    def minRemoveToMakeValid(self, s):
        word_list = list(s)
        stack = list()
        for i, ch in enumerate(s):
            if stack and stack[-1][1] == '(' and ch == ')':
                stack.pop()
            elif ch == '(' or ch == ')':
                stack.append((i, ch))
        for p in stack:
            word_list[p[0]] = ''
        ans = ''.join(word_list)
        return ans


ss = [
    "lee(t(c)o)de)",
    "a)b(c)d",
    "))((",
    "(a(b(c)d)"
]

for st in ss:
    s = Solution().minRemoveToMakeValid(st)
    print(s)
