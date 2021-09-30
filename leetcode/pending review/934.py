from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def mark_island(r, c, marker):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
                return
            if grid[r][c] == 1:
                grid[r][c] = marker
                for dr, dc in directions:
                    mark_island(r + dr, c + dc, marker)

        def expand(r, c, step):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0])):
                return False
            if grid[r][c] == 0:
                grid[r][c] = step + 1
            return grid[r][c] == 1

        marked = False
        # mark first met island as 2
        for i in range(len(grid)):
            if marked:
                break
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    mark_island(i, j, 2)
                    marked = True
                    break

        # expand 2island with increasing steps
        for step in range(2, 2 + len(grid) + len(grid[0]) + 1):
            for i in range(len(grid)):
                for j in range(len(grid[0])):
                    if grid[i][j] == step and any(expand(i + dr, j + dc, step) for dr, dc in directions):
                        return step - 2


cases = [
    [[0, 1], [1, 0]],
    [[0, 1, 0], [0, 0, 0], [0, 0, 1]],
    [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]],
]

for c in cases:
    print(Solution().shortestBridge(c))
