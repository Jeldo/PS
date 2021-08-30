from typing import List


class Solution:
    def minPathSum(self, grid: list):
        for i in range(1, len(grid)):
            grid[i][0] += grid[i - 1][0]
        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j - 1]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]

    def minPathSum2(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        for i in range(1, r):
            grid[i][0] += grid[i - 1][0]
        for i in range(1, c):
            grid[0][i] += grid[0][i - 1]
        for i in range(1, r):
            for j in range(1, c):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]


cases = [
    [[1, 3, 1], [1, 5, 1], [4, 2, 1]],
    [[1, 2, 3], [4, 5, 6]]
]

for c in cases:
    print(Solution().minPathSum(c))
