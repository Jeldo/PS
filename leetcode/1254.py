class Solution:
    def closedIsland(self, grid: list):
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]
        count = 0
        is_island = True
        is_visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def dfs(r, c):
            nonlocal grid, is_island, is_visited
            if is_visited[r][c]:
                return
            is_visited[r][c] = True
            state = True
            for i, j in zip(dr, dc):
                if 0 <= r + i < len(grid) and 0 <= c + j < len(grid[0]):
                    if grid[r+i][c+j] == 0:
                        state = dfs(r+i, c+j)
                else:
                    state = False
                    is_island = False
            return state

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    is_island = dfs(i, j)
                    if is_island:
                        count += 1
                    is_island = True
        return count


cases = [
    [
        [1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 0, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 0]
    ],
    [
        [0, 0, 1, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 1, 1, 1, 0]
    ],
    [
        [1, 1, 1],
        [1, 0, 1],
        [1, 0, 1]
    ],
    [
        [1, 1, 1, 1, 1],
        [1, 0, 1, 0, 1],
        [1, 1, 1, 1, 1]
    ],
    [
        [0, 0, 1, 1, 0, 1, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 0, 1, 1, 1, 0],
        [1, 0, 1, 1, 1, 0, 0, 1, 1, 0],
        [0, 1, 1, 0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 1, 0]
    ]
]

for c in cases:
    s = Solution().closedIsland(c)
    print(s)
