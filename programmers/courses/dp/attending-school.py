def show(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end=' ')
        print()


def solution(m, n, puddles):
    grid = [[0] * (m + 1) for _ in range(n + 1)]
    grid[1][1] = 1
    for p in puddles:
        grid[p[1]][p[0]] = None
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if grid[i][j] != None:
                north = grid[i-1][j] if grid[i-1][j] != None else 0
                west = grid[i][j-1] if grid[i][j-1] != None else 0
                grid[i][j] += north + west
    return grid[n][m] % 1000000007


cases = [
    [4,	3, [[2, 2]]],
    [3, 3, [[2, 2]]],
    [5, 6, [[3, 4], [2, 2], [2, 3]]],
    [1, 7, [[1, 3]]]
]

for c in cases:
    s = solution(*c)
    print(s)
