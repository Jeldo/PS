class Solution:
    def isSubsequence(self, s: str, t: str):
        i = 0
        if not s:
            return True
        for ch in t:
            if ch == s[i]:
                i += 1
            if i == len(s):
                return True
        return False


cases = [
    ["abc",  "ahbgdc"],
    ["axc", "ahbgdc"],
    ["", "ahbgdc"],
]

for c in cases:
    s = Solution().isSubsequence(*c)
    print(s)
