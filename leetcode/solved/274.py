class Solution:
    def hIndex(self, citations: list[int]) -> int:
        h = 0
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if h+1 <= citations[i]:
                h = i+1
        return h


cases = [
    [3, 0, 6, 1, 5],
    [1, 3, 1],
    [0, 0, 0, 0, 0],
]

for c in cases:
    s = Solution().hIndex(c)
    print(s)
