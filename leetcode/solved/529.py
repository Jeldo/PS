'''
Category: DFS
'''


class Solution:
    def updateBoard(self, board: list, click: list):
        dr = [-1, -1, 0, 1, 1, 1, 0, -1]
        dc = [0, 1, 1, 1, 0, -1, -1, -1]
        visited = [[False] * len(board[0]) for _ in range(len(board))]

        def dfs(r, c):
            nonlocal dr, dc, visited
            if visited[r][c]:
                return
            visited[r][c] = True
            mine_count = 0
            for i, j in zip(dr, dc):
                if 0 <= r + i < len(board) and 0 <= c + j < len(board[0]):
                    if board[r+i][c+j] == 'M':
                        mine_count += 1
            if mine_count == 0:
                board[r][c] = 'B'
            else:
                board[r][c] = str(mine_count)
                return
            for i, j in zip(dr, dc):
                if 0 <= r + i < len(board) and 0 <= c + j < len(board[0]):
                    if board[r+i][c+j] == 'E':
                        dfs(r+i, c+j)

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else:
            dfs(click[0], click[1])
        return board


cases = [
    [
        [
            ['E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'M', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E']
        ],
        [3, 0]
    ],
    [
        [
            ['B', '1', 'E', '1', 'B'],
            ['B', '1', 'M', '1', 'B'],
            ['B', '1', '1', '1', 'B'],
            ['B', 'B', 'B', 'B', 'B']
        ],
        [1, 2]
    ]
]

for c in cases:
    s = Solution().updateBoard(c[0], c[1])
    for r in range(len(s)):
        for c in range(len(s[0])):
            print(s[r][c], end=' ')
        print()
    print()
