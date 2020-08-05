class Solution:
    def maxAreaOfIsland(self, grid: list):
        cur_size = 0
        max_size = 0
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        def dfs(r, c):
            nonlocal cur_size, dr, dc
            cur_size += 1
            grid[r][c] = 0
            for i, j in zip(dr, dc):
                if 0 <= r + i < len(grid) and 0 <= c + j < len(grid[0]) and grid[r+i][c+j] == 1:
                    dfs(r + i, c + j)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    dfs(r, c)
                    max_size = max(max_size, cur_size)
                    cur_size = 0
        return max_size


cases = [
    [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
    ],
    [
        [0, 0, 0, 0, 0, 0, 0, 0]
    ],
    [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]
    ],
    [
        [0, 1],
        [1, 1]
    ],
    [[0]],
    [[1]]
]

for c in cases:
    s = Solution().maxAreaOfIsland(c)
    print(s)


# grid = [[0, 0, 0],
#         [0, 0, 0]]
# a = [[0] * len(grid[0]) for _ in range(len(grid))]
# print(a)
