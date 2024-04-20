class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def dfs(r, c):
            nonlocal max_r, max_c
            if 0 <= r < len(land) and 0 <= c < len(land[0]) and land[r][c] == 0:
                return
            if not (0 <= r < len(land) and 0 <= c < len(land[0])):
                return
            max_r = max(max_r, r)
            max_c = max(max_c, c)
            land[r][c] = 0
            for d in directions:
                dfs(r+d[0], c+d[1])

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        groups = []
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1:
                    max_r, max_c = i, j
                    dfs(i, j)
                    groups.append([i, j, max_r, max_c])

        return groups
