class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        def set_zeros(r, c):
            for i in range(len(matrix)):
                matrix[i][c] = 0
            for i in range(len(matrix[0])):
                matrix[r][i] = 0

        zeros = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    zeros.append((i, j))
        for r, c in zeros:
            set_zeros(r, c)


cases = [
    [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
    [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],
]

for c in cases:
    res = Solution().setZeroes(c)
    print(res)
