from collections import Counter


class Solution:
    # Time: O(n)
    def minSteps(self, s, t):
        ss = Counter(s)
        tt = Counter(t)
        return sum([val for val in (ss-tt).values()])


cases = [
    ["bab", "aba"],
    ["leetcode", "practice"],
    ["anagram", "mangaar"],
    ["xxyyzz", "xxyyzz"],
    ["friend", "family"]
]

for c in cases:
    s = Solution().minSteps(c[0], c[1])
    print(s)
