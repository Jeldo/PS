from typing import List

# O(m*n)


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                pool = []
                for k in range(-1, 2):
                    if 0 <= j + k < len(matrix[0]):
                        pool.append(matrix[i-1][j+k])
                matrix[i][j] += min(pool)

        return min(matrix[-1])


cases = [
    [[2, 1, 3], [6, 5, 4], [7, 8, 9]],
    [[-19, 57], [-40, -5]],
]

for c in cases:
    print(Solution().minFallingPathSum(c))
