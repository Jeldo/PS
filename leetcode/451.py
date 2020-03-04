'''
Time Complexity: O(nlogn)
'''
from collections import Counter
import heapq


class Solution:
    # O(nlogn)
    def frequencySort(self, s):
        alpha_heap = list()
        alpha_dict = Counter(s)                         # O(n)
        for key, val in alpha_dict.items():             # aggregate n length string to k length dict ( k <= n )
            heapq.heappush(alpha_heap, (-val, key))     # O(logn)
        answer = ''
        while alpha_heap:                               # O(n)
            val, key = heapq.heappop(alpha_heap)        # O(logn)
            answer += key * -val
        return answer

    # O(nlogn)
    def frequencySort2(self, s):
        alpha_dict = Counter(s)
        alpha_list = sorted([(val, key)     # O(nlogn)
                             for key, val in alpha_dict.items()], reverse=True)
        answer = ''.join([key * val for val, key in alpha_list])
        return answer

    # O(nlogn)
    def frequencySort3(self, s):
        alpha_dict = Counter(s)
        alpha_heap = [(-val, key) for key, val in alpha_dict.items()]   # O(n)
        heapq.heapify(alpha_heap)   # O(logn)
        answer = ''
        while alpha_heap:
            val, key = heapq.heappop(alpha_heap)
            answer += key * -val
        return answer


ques = ['tree', 'cccaaa', 'Aabb']
for q in ques:
    s = Solution().frequencySort2(q)
    print(s)
