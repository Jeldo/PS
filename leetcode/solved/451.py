'''
Time Complexity: O(nlogn)
'''
import heapq
from collections import Counter


class Solution:
    def frequencySort(self, s: str):
        res = ''
        l = [(-v, k) for k, v in Counter(s).items()]
        heapq.heapify(l)
        while l:
            v, k = heapq.heappop(l)
            res += -v * k
        return res


cases = [
    "tree",
    "cccaaa",
    "Aabb",
    "abaccadeeefaafcc"
]

for c in cases:
    s = Solution().frequencySort(c)
    print(s)
