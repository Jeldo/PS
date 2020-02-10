'''
- DFS in minesweeper
'''


class Solution:
    direction_row = [-1, -1, 0, 1, 1, 1, 0, -1]
    direction_column = [0, 1, 1, 1, 0, -1, -1, -1]

    def print_board(self, board):
        for r in range(len(board)):
            for c in range(len(board[0])):
                print(board[r][c], end=' ')
            print()

    def updateBoard(self, board, click):
        row, col = len(board), len(board[0])
        visited = [[False]*col for _ in range(row)]
        click_r, click_c = click[0], click[1]

        def eight_flood_fill(board, visited, r, c):
            visited[r][c] = True
            # find adjacent mines
            mines = 0
            for dr, dc in zip(Solution.direction_row, Solution.direction_column):
                if 0 <= r + dr and r + dr < row and 0 <= c + dc and c + dc < col:
                    if board[r + dr][c + dc] == 'M':
                        mines += 1
            if mines > 0:
                board[r][c] = str(mines)
            # find adjacent blanks
            elif mines == 0:
                board[r][c] = 'B'
                for dr, dc in zip(Solution.direction_row, Solution.direction_column):
                    if 0 <= r + dr and r + dr < row and 0 <= c + dc and c + dc < col and not visited[r + dr][c + dc]:
                        eight_flood_fill(board, visited, r + dr, c + dc)

        if board[click_r][click_c] == 'M':
            board[click_r][click_c] = 'X'
            # self.print_board(visited)
            return board
        else:
            eight_flood_fill(board, visited, click_r, click_c)
            # self.print_board(visited)
            return board


b = [["E", "E", "E", "E", "E"], ["E", "E", "M", "E", "E"],
     ["E", "E", "E", "E", "E"], ["E", "E", "E", "E", "E"]]
c = [3, 0]
bb = [['B', '1', 'E', '1', 'B'],
      ['B', '1', 'M', '1', 'B'],
      ['B', '1', '1', '1', 'B'],
      ['B', 'B', 'B', 'B', 'B']]
cc = [1, 2]
s = Solution()

s.print_board(b)
print()

updated_board = s.updateBoard(b, c)
s.print_board(updated_board)
