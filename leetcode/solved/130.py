from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        row, col = len(board), len(board[0])

        def dfs(r, c):
            if not (0 <= r < row and 0 <= c < col):
                return
            if board[r][c] == 'X' or board[r][c] == '-':
                return
            board[r][c] = '-'
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for i in range(row):
            for j in range(col):
                if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                    dfs(i, j)

        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '-':
                    board[i][j] = 'O'


cases = [
    [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]],
    [["X"]],
]

for c in cases:
    print(Solution().solve(c))
