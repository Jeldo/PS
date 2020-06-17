'''
Category: String
'''


class Solution:
    def checkIfCanBreak(self, s1: str, s2: str):
        s1, s2 = sorted(s1), sorted(s2)
        c1, c2 = True, True
        for i, j in zip(s1, s2):
            if i > j:
                c1 = False
            if i < j:
                c2 = False
        return c1 or c2


cases = [
    ["abc", "xya"],
    ["abe", "acd"],
    ["leetcodee", "interview"]
]

for c in cases:
    s = Solution().checkIfCanBreak(c[0], c[1])
    print(s)
