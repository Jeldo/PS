'''
Brute force 2D array
dumbass :P
'''


class Solution:
    direction_row = [-1, -1, 0, 1, 1, 1, 0, -1]
    direction_column = [0, 1, 1, 1, 0, -1, -1, -1]

    def print_board(self, board):
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                print(board[i][j], end=' ')
            print()
        print()

    def queensAttacktheKing(self, queens, king):
        board = [[False]*8 for _ in range(0, 8)]
        for q in queens:
            board[q[0]][q[1]] = 'Q'
        kingslayer = list()

        def is_queen(pos):
            return True if board[pos[0]][pos[1]] == 'Q' else False

        def is_safe(pos):
            return True if 0 <= pos[0] < 8 and 0 <= pos[1] < 8 else False

        def find_queen_by_clock_wise(pos):
            for dr, dc in zip(Solution.direction_row, Solution.direction_column):
                next_pos = [pos[0]-dr, pos[1]-dc]
                while is_safe(next_pos):
                    if is_queen(next_pos):
                        kingslayer.append(next_pos)
                        break
                    else:
                        next_pos[0] -= dr
                        next_pos[1] -= dc

        find_queen_by_clock_wise(king)
        return kingslayer


q = [[0, 1], [1, 0], [4, 0], [0, 4], [3, 3], [2, 4]]
k = [3, 1]
qq = [[5, 6], [7, 7], [2, 1], [0, 7], [1, 6], [5, 1], [3, 7], [0, 3], [4, 0], [1, 2], [6, 3], [5, 0], [0, 4], [2, 2], [1, 1], [6, 4], [5, 4], [
    0, 0], [2, 6], [4, 5], [5, 2], [1, 4], [7, 5], [2, 3], [0, 5], [4, 2], [1, 0], [2, 7], [0, 1], [4, 6], [6, 1], [0, 6], [4, 3], [1, 7]]
kk = [3, 4]
s = Solution().queensAttacktheKing(qq, kk)
print(s)
