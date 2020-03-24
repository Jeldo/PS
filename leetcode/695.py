class Solution:
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    def maxAreaOfIsland(self, grid):
        max_area = 0

        def dfs(row, col):
            nonlocal sub_area
            grid[row][col] = 0
            sub_area += 1
            for r, c in zip(Solution.dr, Solution.dc):
                if 0 <= row + r < len(grid) and 0 <= col + c < len(grid[0]) and grid[row+r][col+c] == 1:
                    dfs(row+r, col+c)

        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    sub_area = 0
                    dfs(i, j)
                    if max_area < sub_area:
                        max_area = sub_area

        return max_area


islands = [
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
    ]
]

for i in islands:
    s = Solution().maxAreaOfIsland(i)
    print(s)
