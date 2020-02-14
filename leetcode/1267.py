class Solution:
    direction_row = [-1, 0, 1, 0]
    direction_column = [0, 1, 0, -1]

    def countServers(self, grid):
        width, height = len(grid[0]), len(grid)
        total = 0

        def is_safe(position):
            return True if 0 <= position[0] < height and 0 <= position[1] < width else False

        def find_server(position):
            nonlocal total
            is_found = False
            for dr, dc in zip(Solution.direction_row, Solution.direction_column):
                next_position = [position[0]+dr, position[1]+dc]
                while is_safe(next_position) and not is_found:
                    if grid[next_position[0]][next_position[1]] == 1:
                        total += 1
                        is_found = True
                    next_position[0] += dr
                    next_position[1] += dc
                if is_found:
                    break

        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    find_server([i, j])

        return total


g1 = [[1, 0], [0, 1]]                                           # 0
g2 = [[1, 0], [1, 1]]                                           # 3
g3 = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]   # 4
g4 = [[1, 0, 0, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0]]        # 3
s = Solution().countServers(g4)
print(s)
