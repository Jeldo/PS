'''
Backtracking
'''


class Solution:
    def getMaximumGold(self, grid: list) -> int:
        dr = [-1, 0, 1, 0]
        dc = [0, 1, 0, -1]

        def dfs(r, c):
            nonlocal cur_gold, max_gold
            if not(0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] > 0):
                return
            origin_gold = grid[r][c]
            cur_gold += origin_gold
            max_gold = max(max_gold, cur_gold)
            grid[r][c] = 0
            for i, j in zip(dr, dc):
                dfs(r+i, c+j)
            cur_gold -= origin_gold
            grid[r][c] = origin_gold

        cur_gold = 0
        max_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                dfs(i, j)
        return max_gold


cases = [
    [[0, 6, 0], [5, 8, 7], [0, 9, 0]],
    [[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]
]

for c in cases:
    s = Solution().getMaximumGold(c)
    print(s)
