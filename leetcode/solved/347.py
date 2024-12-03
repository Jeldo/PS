from collections import Counter
import heapq


class Solution:
    # O(nlogn)
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        l = [(key, value) for key, value in Counter(nums).items()]  # O(n)
        return [key for _, key in heapq.nlargest(n=k, iterable=l)]  # O(nlogn)


cases = [
    [[1, 1, 1, 2, 2, 3], 2],
    [[1], 1],
]

for c in cases:
    print(Solution().topKFrequent(*c))
