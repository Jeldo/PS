'''
Category: heap
'''
import heapq
from collections import Counter


class Solution:
    def topKFrequent(self, nums: list, k: int):
        l = [(-value, key) for key, value in Counter(nums).items()]
        return [key for value, key in heapq.nsmallest(k, l)]

    # using max-heap, beats 65%
    def topKFrequent1(self, nums, k):
        num_dict = dict()
        for n in nums:
            if n not in num_dict.keys():
                num_dict[n] = 1
            else:
                num_dict[n] += 1
        frequency_list = [(-num_dict[n], n) for n in num_dict.keys()]
        heapq.heapify(frequency_list)
        return [heapq.heappop(frequency_list)[1] for _ in range(k)]

    # using min-heap, keeping length of count_list at k, beats 99% time
    def topKFrequent2(self, nums, k):
        num_dict = Counter(nums)
        frequency_list = list()
        for key, val in num_dict.items():
            if len(frequency_list) < k:
                heapq.heappush(frequency_list, (val, key))
            else:
                heapq.heappushpop(frequency_list, (val, key))
        return [x[1] for x in frequency_list]

    # using only dictionary, beats 90%
    def topKFrequent3(self, nums, k):
        frequency_list = Counter(nums)
        sorted_list = sorted(frequency_list.items(), key=lambda x: -x[1])
        return [sorted_list[key][0] for key in range(k)]

    # using library, beats 65%
    def topKFrequent4(self, nums, k):
        return [x[0] for x in Counter(nums).most_common(k)]


cases = [
    [[1, 1, 1, 2, 2, 3], 2],
    [[1], 1]
]

for c in cases:
    s = Solution().topKFrequent(c[0], c[1])
    print(s)
