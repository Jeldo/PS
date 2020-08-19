'''
Category: Hash Table
'''
from collections import defaultdict
import heapq


class Solution:
    def largestValsFromLabels(self, values: list, labels: list, num_wanted: int, use_limit: int):
        dd = defaultdict(list)
        for v, l in zip(values, labels):
            dd[l].append(v)
        candidates = []
        for k, v in dd.items():
            candidates.extend(sorted(v, reverse=True)[:use_limit])
        return sum(sorted(candidates, reverse=True)[:num_wanted])


cases = [
    [[5, 4, 3, 2, 1],  [1, 1, 2, 2, 3],  3, 1],
    [[5, 4, 3, 2, 1], [1, 3, 3, 3, 2], 3,  2],
    [[9, 8, 8, 6, 7],  [0, 0, 0, 1, 1], 3, 1],
    [[9, 8, 8, 7, 6],  [0, 0, 0, 1, 1],  3, 2],
    [[4, 7, 4, 6, 3], [2, 0, 0, 2, 2], 1, 2]
]

for c in cases:
    s = Solution().largestValsFromLabels(*c)
    print(s)
