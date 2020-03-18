class Solution:
    # Brute force: not scalable
    def countSquares(self, matrix):
        m, n = len(matrix), len(matrix[0])
        k = min(m, n)
        count = 0
        for row in range(0, m):
            for col in range(0, n):
                if matrix[row][col] == 1:
                    for i in range(0, k):
                        is_square = True
                        print('length: {}'.format(i+1))
                        print('point: ({}, {})'.format(row, col))
                        if row + i < m and col + i < n:
                            for sub_row in range(0, i+1):
                                if is_square == False:
                                    break
                                for sub_col in range(0, i+1):
                                    if is_square == False:
                                        break
                                    if matrix[row+sub_row][col+sub_col] == 0:
                                        is_square = False
                                    print('sub point: ({}, {})'.format(
                                        row+sub_row, col+sub_col))
                        else:
                            is_square = False
                        if is_square == True:
                            count += 1
        return count


matrixies = [
    [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ],
    [
        [1, 0, 1],
        [1, 1, 0],
        [1, 1, 0]
    ],
    [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ],
]
# 15, 7, 14
for m in matrixies:
    s = Solution().countSquares(m)
    print(s)
