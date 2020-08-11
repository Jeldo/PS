'''
Category: heap
'''
import heapq


class Solution:
    def kthSmallest(self, matrix: list, k: int):
        hq = []
        for r in matrix:
            for c in r:
                heapq.heappush(hq, c)
        return heapq.nsmallest(k, hq)[-1]

    def kthSmallest2(self, matrix, k):
        result, heap = None, []
        heapq.heappush(heap, (matrix[0][0], 0, 0))
        while k > 0:
            result, i, j = heapq.heappop(heap)
            if i == 0 and j + 1 < len(matrix):
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
            if i + 1 < len(matrix):
                heapq.heappush(heap, (matrix[i + 1][j], i + 1, j))
            k -= 1
        return result


cases = [
    [
        [
            [1,  5,  9],
            [10, 11, 13],
            [12, 13, 15]
        ],
        8
    ],

]

for c in cases:
    s = Solution().kthSmallest2(c[0], c[1])
    print(s)
