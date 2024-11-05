class Solution:
    def minChanges(self, s: str) -> int:
        count = 0
        for i in range(1, len(s), 2):
            if s[i-1] != s[i]:
                count += 1
        return count


cases = [
    "1001",
    "10",
    "0000",
]

for c in cases:
    print(Solution().minChanges(c))
