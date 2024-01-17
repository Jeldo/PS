from collections import Counter
from typing import List


class Solution:
    # O(n)
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurrences = Counter(arr)
        values = set()
        for v in occurrences.values():
            if v in values:
                return False
            values.add(v)
        return True


cases = [
    [1, 2, 2, 1, 1, 3],
    [1, 2],
    [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
]

for c in cases:
    print(Solution().uniqueOccurrences(c))
