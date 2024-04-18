class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        perimeter = 0
        def dfs(i, j):
            nonlocal perimeter
            if (i, j) in visited:
                return
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 0:
                perimeter += 1
                return
            if not(0 <= i < len(grid) and 0 <= j < len(grid[0])):
                perimeter += 1
                return
            visited.add((i, j))
            for d in directions:
                dfs(i+d[0], j+d[1])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    return perimeter
