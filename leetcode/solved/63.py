class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list):
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        if obstacleGrid[r - 1][c - 1] == 1:
            return 0

        dp = [[0] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = -1

        for i in range(r):
            if dp[i][0] == -1:
                break
            dp[i][0] = 1

        for j in range(c):
            if dp[0][j] == -1:
                break
            dp[0][j] = 1

        for i in range(1, r):
            for j in range(1, c):
                if dp[i][j] != -1:
                    up = dp[i - 1][j] if dp[i - 1][j] != -1 else 0
                    left = dp[i][j - 1] if dp[i][j - 1] != -1 else 0
                    dp[i][j] = up + left

        return dp[-1][-1]


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
