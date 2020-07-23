'''
Category: Stack
Time Complexity: O(n)
'''


class Solution:
    def removeDuplicates(self, s: str, k: int):
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                n = stack[-1][1] + 1
                stack.append((c, n))
                if n == k:
                    for _ in range(k):
                        stack.pop()
            else:
                stack.append((c, 1))
        return ''.join([c for c, i in stack])

    def removeDuplicates2(self, s: str, k: int):
        stack = []
        for c in s:
            if stack and stack[-1][0] == c:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([c, 1])
        return ''.join(c * i for c, i in stack)


cases = [
    ("abcd", 2),
    ("deeedbbcccbdaa", 3),
    ("pbbcggttciiippooaais", 2)
]

for c in cases:
    s = Solution().removeDuplicates2(c[0], c[1])
    print(s)
