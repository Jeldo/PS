class Solution:
    def maxEqualRowsAfterFlips(self, matrix: list):
        return 0


cases = [
    [[0, 1], [1, 1]],
    [[0, 1], [1, 0]],
    [[0, 0, 0], [0, 0, 1], [1, 1, 0]]
]

for c in cases:
    s = Solution().findMinFibonacciNumbers(c)
    print(s)
