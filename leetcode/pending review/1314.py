class Solution:
    def matrixBlockSum(self, mat: list, K: int):
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                up, left = 0, 0
                if 0 <= i-1 < len(mat):
                    up = mat[i-1][j]
                if 0 <= j-1 < len(mat[0]):
                    left = mat[i][j-1]
                mat[i][j] += up + left
        return mat

    def matrixBlockSum2(self, mat: list, K: int):
        def calc_surround(r, c):
            nonlocal mat, K
            total = 0
            for i in range(r-K, r+K+1):
                for j in range(c-K, c+K+1):
                    if 0 <= i < len(mat) and 0 <= j < len(mat[0]):
                        total += mat[i][j]
            return total

        def calc_left_column(r, c):
            nonlocal mat, K
            total = 0
            for i in range(r-K, r+K+1):
                if 0 <= i < len(mat) and 0 <= c - K - 1 < len(mat[0]):
                    total += mat[i][c-K-1]
            return total

        def calc_right_column(r, c):
            nonlocal mat, K
            total = 0
            for i in range(r-K, r+K+1):
                if 0 <= i < len(mat) and 0 <= c + K < len(mat[0]):
                    total += mat[i][c+K]
            return total

        grid = [[0] * len(mat[0]) for _ in range(len(mat))]
        for i in range(len(mat)):
            cache = 0
            for j in range(len(mat[0])):
                if j == 0:
                    cache = calc_surround(i, j)
                else:
                    left_c = calc_left_column(i, j)
                    right_c = calc_right_column(i, j)
                    cache = cache - left_c + right_c
                grid[i][j] = cache
        return grid


cases = [
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1],
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2]
]

for c in cases:
    s = Solution().matrixBlockSum(*c)
    print(s)
