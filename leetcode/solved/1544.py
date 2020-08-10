class Solution:
    def makeGood(self, s: str):
        stack = []
        for ch in s:
            if stack and (stack[-1] == ch.lower() and (stack[-1].islower() and ch.isupper())):
                stack.pop()
            elif stack and (stack[-1] == ch.upper() and (stack[-1].isupper() and ch.islower())):
                stack.pop()
            else:
                stack.append(ch)
        return ''.join(stack)


cases = [
    "leEeetcode",
    "abBAcC",
    "Pp",
    "kkdsFuqUfSDKK"
]

for c in cases:
    s = Solution().makeGood(c)
    print(s)
