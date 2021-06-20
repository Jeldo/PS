class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: list[int]) -> list[list[int]]:
        if upper + lower != sum(colsum):
            return []
        matrix = [[0] * len(colsum) for _ in range(2)]
        for i in range(len(colsum)):
            if colsum[i] == 2:
                upper -= 1
                lower -= 1
                matrix[0][i], matrix[1][i] = 1, 1
                colsum[i] = 0
        if upper < 0 or lower < 0:
            return []

        for i in range(2):
            for j in range(len(colsum)):
                if i == 0 and colsum[j] > 0 and 0 < upper:
                    matrix[i][j] = 1
                    colsum[j] -= 1
                    upper -= 1
                elif i == 1 and colsum[j] > 0 and 0 < lower:
                    matrix[i][j] = 1
                    colsum[j] -= 1
                    lower += 1
        return matrix


cases = [
    [2, 1, [1, 1, 1]],
    [2, 3, [2, 2, 1, 1]],
    [5, 5, [2, 1, 2, 0, 1, 0, 1, 2, 0, 1]],
    [9, 2, [0, 1, 2, 0, 0, 0, 0, 0, 2, 1, 2, 1, 2]],
]

for c in cases:
    res = Solution().reconstructMatrix(*c)
    print(res)
