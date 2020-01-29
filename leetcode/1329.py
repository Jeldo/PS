'''
Time Complexity: O(n**2)
'''


class Solution:
    def diagonalSort(self, mat):
        start = list()
        m = len(mat)
        n = len(mat[0])
        for i in range(n):
            start.append((0, n-i-1))
        for i in range(m):
            start.append((i+1, 0))
        for i in range(len(start)):
            row, col = start[i][0], start[i][1]
            temp = list()
            while row < m and col < n:
                temp.append(mat[row][col])
                row += 1
                col += 1
            temp.sort()
            row, col = start[i][0], start[i][1]
            for i in range(len(temp)):
                mat[row+i][col+i] = temp[i]
        return mat


mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
s = Solution().diagonalSort(mat)
for r in range(0, len(s)):
    for c in range(0, len(s[0])):
        print(s[r][c], end=' ')
    print()
