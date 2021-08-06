import bisect


class Solution:
    # O(logM + logN), m: length of row, n: length of column
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        def index(a, x):
            i = bisect.bisect_left(a, x)
            if i != len(a) and a[i] == x:
                return True
            return False

        if target < matrix[0][0] or matrix[-1][-1] < target:
            return False
        t, b, l, f = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        row = 0

        while t <= b:
            mid = (t + b) // 2
            if matrix[mid][0] <= target:
                t = mid + 1
                row = mid
            elif matrix[mid][0] > target:
                b = mid - 1

        return index(matrix[row], target)

    # O(N)
    def searchMatrix2(self, matrix: list[list[int]], target: int) -> bool:
        def index(a, x):
            i = bisect.bisect_left(a, x)
            if i != len(a) and a[i] == x:
                return True
            return False

        row = 0
        for r in range(len(matrix)):
            if matrix[r][0] <= target:
                row = r
            else:
                break
        return index(matrix[row], target)


cases = [
    [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3],
    [[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13],
    [[[1, 2], [3, 4]], -1],
    [[[1, 2], [3, 4]], 10],
    [[[1, 2, 4], [5, 8, 10]], 8],
]

for c in cases:
    print(Solution().searchMatrix(*c))
