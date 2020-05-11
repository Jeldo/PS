'''
Category: DP
'''


class Solution:
    def uniquePaths(self, m: int, n: int):
        grid = [[0]*m for _ in range(n)]
        for i in range(m):
            grid[0][i] = 1
        for i in range(n):
            grid[i][0] = 1
        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[-1][-1]


cases = [
    (3, 2),
    (7, 3),
    (1, 1),
    (1, 2),
    (2, 1),
    (2, 2)
]

for c in cases:
    s = Solution().uniquePaths(c[0], c[1])
    print(s)
