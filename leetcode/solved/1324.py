'''
Category: String
'''


class Solution:
    def printVertically(self, s: str):
        s = s.split()
        max_len = len(max(s, key=lambda x: len(x)))
        res = []
        for i in range(max_len):
            temp = ''
            for j in range(len(s)):
                if i + 1 <= len(s[j]):
                    temp += s[j][i]
                else:
                    temp += ' '
            res.append(temp.rstrip())
        return res


cases = [
    "HOW ARE YOU",
    "CONTEST IS COMING",
    "TO BE OR NOT TO BE",
]

for c in cases:
    s = Solution().printVertically(c)
    print(s)
