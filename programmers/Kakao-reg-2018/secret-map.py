def solution(n, arr1, arr2):
    grid = [[' '] * n for _ in range(n)]
    new_map = []

    def mark_grid(arr):
        for i in range(len(arr)):
            col = bin(arr[i])[2:]
            col = (n - len(col)) * '0' + col
            for j in range(len(col)):
                if col[j] == '1':
                    grid[i][j] = '#'
    mark_grid(arr1)
    mark_grid(arr2)
    for row in grid:
        new_map.append(''.join(row))
    return new_map


cases = [
    [5,	[9, 20, 28, 18, 11], [30, 1, 21, 17, 28]],
    [6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]]
]

for c in cases:
    s = solution(*c)
    print(s)
