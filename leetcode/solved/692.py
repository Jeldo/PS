import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        q = [(-v, k) for k, v in Counter(words).items()]
        smallest = heapq.nsmallest(k, q)
        return [f[1] for f in smallest]


cases = [
    [["i", "love", "leetcode", "i", "love", "coding"], 2],
    [["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4],
]

for c in cases:
    print(Solution().topKFrequent(*c))
