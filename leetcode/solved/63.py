'''
Category: Dynamic Programming
'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list):
        grid = [[0]*len(obstacleGrid[0]) for _ in range(len(obstacleGrid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = -1

        for i in range(len(grid)):
            if grid[i][0] == -1:
                break
            grid[i][0] = 1

        for j in range(len(grid[0])):
            if grid[0][j] == -1:
                break
            grid[0][j] = 1

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                if grid[i][j] != -1:
                    up = grid[i-1][j] if grid[i-1][j] != -1 else 0
                    left = grid[i][j-1] if grid[i][j-1] != -1 else 0
                    grid[i][j] = up + left
        return grid[-1][-1] if grid[-1][-1] != -1 else 0


cases = [
    [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ],
    [
        [0, 1, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 0]
    ]
]

for c in cases:
    s = Solution().uniquePathsWithObstacles(c)
    print(s)
