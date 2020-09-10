'''
Category: Two Pointers
Time Complexity: O(n)
'''
from queue import deque


class Solution:
    def sortedSquares(self, A: list):
        q = deque([])
        l, r = 0, len(A)-1
        while l <= r:
            left, right = abs(A[l]), abs(A[r])
            if left < right:
                q.appendleft(right ** 2)
                r -= 1
            else:
                q.appendleft(left ** 2)
                l += 1
        return q


cases = [
    [-4, -1, 0, 3, 10],
    [-7, -3, 2, 3, 11]
]

for c in cases:
    s = Solution().sortedSquares(c)
    print(s)
