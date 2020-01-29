'''
Time Complexity: O(n**2)
'''
import heapq


class Solution:
    def diagonalSort(self, mat):
        starting_points = list()
        m, n = len(mat), len(mat[0])
        for i in range(n+m-1):
            if i < n:
                starting_points.append((0, n-i-1))
            else:
                starting_points.append((i-n+1, 0))
        for i in range(len(starting_points)):
            row, col = starting_points[i][0], starting_points[i][1]
            diagonal_elements_q = list()
            while row < m and col < n:
                heapq.heappush(diagonal_elements_q, mat[row][col])
                row += 1
                col += 1
            row, col = starting_points[i][0], starting_points[i][1]
            j = 0
            while len(diagonal_elements_q) > 0:
                mat[row+j][col+j] = heapq.heappop(diagonal_elements_q)
                j += 1
        return mat


mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
s = Solution().diagonalSort(mat)

for r in range(0, len(s)):
    for c in range(0, len(s[0])):
        print(s[r][c], end=' ')
    print()
