class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def dfs(r, c):
            nonlocal area
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])) or grid[r][c] == 0:
                return
            grid[r][c] = 0
            area += 1
            for dr, dc in direction:
                dfs(r + dr, c + dc)

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = 0
                    dfs(i, j)
                    max_area = max(max_area, area)

        return max_area


cases = [
    [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0, 0, 0]],
]

for c in cases:
    print(Solution().maxAreaOfIsland(c))
