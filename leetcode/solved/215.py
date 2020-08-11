'''
Category: heap
'''
import heapq


class Solution:
    def findKthLargest(self, nums: list, k: int):
        return heapq.nlargest(k, nums)[-1]


cases = [
    [[3, 2, 1, 5, 6, 4], 2],
    [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4]
]

for c in cases:
    s = Solution().findKthLargest(c[0], c[1])
    print(s)
