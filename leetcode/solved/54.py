class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        order = []
        direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i, heading = 0, 0
        r, c = 0, 0
        while i < len(matrix) * len(matrix[0]):
            order.append(matrix[r][c])
            matrix[r][c] = None
            next_r = r + direction[heading][0]
            next_c = c + direction[heading][1]
            i += 1
            if not (0 <= next_r < len(matrix) and 0 <= next_c < len(matrix[0])) or matrix[next_r][next_c] is None:
                heading = (heading + 1) % 4
                next_r = r + direction[heading][0]
                next_c = c + direction[heading][1]
            r, c = next_r, next_c

        return order


cases = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
    [[1]],
    [[1, 2], [3, 4]],
]

for c in cases:
    print(Solution().spiralOrder(c))
