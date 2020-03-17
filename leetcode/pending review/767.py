from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, S: str):
        heap_list = [(-value, key) for key, value in Counter(S).items()]
        heapq.heapify(heap_list)
        print(heap_list)
        if -heap_list[0][0] > (len(S) + 1) / 2:
            return ''
        ans = list()
        while len(heap_list) >= 2:
            value_first, ch_first = heapq.heappop(heap_list)
            value_second, ch_second = heapq.heappop(heap_list)
            ans.extend([ch_first, ch_second])
            if value_first + 1:
                heapq.heappush(heap_list, (value_first+1, ch_first))
            if value_second + 1:
                heapq.heappush(heap_list, (value_second+1, ch_second))
        return ''.join(ans) + (heap_list[0][1] if heap_list else '')


strings = ['aab', 'aaab', "kkkkzrkatkwpkkkktrq"]

for s in strings:
    sol = Solution().reorganizeString(s)
    print('res:', sol)
