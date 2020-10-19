import copy


def solution(m, n, board):
    grid = [['' for _ in range(n)] for _ in range(m)]
    new_grid = copy.deepcopy(grid)
    for i in range(m):
        for j in range(n):
            grid[i][j] = board[i][j]

    for i in range(m-1):
        for j in range(n-1):
            char = grid[i][j]
            is_valid = True
            for r in range(2):
                for c in range(2):
                    if grid[i+r][j+c] != char:
                        is_valid = False
            if is_valid:

    return 0


cases = [
    [4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF']],
    [6, 6, ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']]
]

for c in cases:
    s = solution(*c)
    print(s)
