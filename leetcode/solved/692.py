'''
Category: heap
'''
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, words: list, k):
        c = [(-v, key) for key, v in Counter(words).items()]
        return [x[1] for x in heapq.nsmallest(k, c)]


cases = [
    [["love", "i", "leetcode", "i", "love", "coding"], 2],
    [["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4]
]

for c in cases:
    s = Solution().topKFrequent(c[0], c[1])
    print(s)
