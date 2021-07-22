class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            for dr, dc in direction:
                dfs(r + dr, c + dc)

        island = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    island += 1
                    dfs(i, j)

        return island


cases = [
    [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ],
    [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ],
    [['1']],
    [['0']],
]

for c in cases:
    res = Solution().numIslands(c)
    print(res)
