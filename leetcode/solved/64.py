'''
Category: Dynamic Programming
let (m, n) is the length of row and column of a grid.
Time Complexity: O(m*n)
Space Complexity: O(m*n)
'''


class Solution:
    # use original grid
    def minPathSum(self, grid):
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if i == 0 and j > 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0 and i > 0:
                    grid[i][j] += grid[i-1][j]
                elif i > 0 and j > 0:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

    # use new table to mark a cost
    def minPathSum2(self, grid):
        cost = [([0]*len(grid[0]))for _ in range(0, len(grid))]
        cost[0][0] = grid[0][0]
        for i in range(0, len(cost)):
            for j in range(0, len(cost[0])):
                if i == 0 and j > 0:
                    cost[i][j] = grid[i][j] + cost[i][j-1]
                elif j == 0 and i > 0:
                    cost[i][j] = grid[i][j] + cost[i-1][j]
                else:
                    cost[i][j] = grid[i][j] + min(cost[i-1][j], cost[i][j-1])
        return cost[-1][-1]


cases = [
    [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ],
    [
        [1, 2, 4, 1],
        [1, 3, 1, 2],
        [3, 1, 2, 1]
    ],
    [
        [1]
    ],
    [
        [1, 0],
        [1, 1]
    ],
    [
        [1],
        [3]
    ],
    [
        [1, 2]
    ]
]

for c in cases:
    s = Solution().minPathSum(c)
    print(s)
