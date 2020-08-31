'''
Category: Dynamic Programming
let (m, n) is the length of row and column of a grid.
Time Complexity: O(m*n)
Space Complexity: O(m*n)
'''


class Solution:
    def minPathSum(self, grid: list):
        for i in range(1, len(grid)):
            grid[i][0] += grid[i-1][0]
        for j in range(1, len(grid[0])):
            grid[0][j] += grid[0][j-1]
        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]


cases = [
    [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
]

for c in cases:
    s = Solution().minPathSum(c)
    print(s)
