'''
Category: String
'''


class Solution:
    def numberOfSubstrings(self, s: str):
        count = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                sub = s[i:j]
                if 'a' in sub and 'b' in sub and 'c' in sub:
                    count += 1
        return count

    # brute force, time limit exceeded
    def numberOfSubstrings2(self, s: str):
        count = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                sub = s[i:j]
                if 'a' in sub and 'b' in sub and 'c' in sub:
                    count += 1
        return count


cases = [
    "abcabc",
    "aaacb",
    "abc"
]

for c in cases:
    s = Solution().numberOfSubstrings(c)
    print(s)
