'''
Time Complexity: O(nlogn)
'''

import heapq


class Solution:
    def findKthLargest(self, nums, k):
        # equivalent to: sorted(iterable, reverse=True)[:n]
        return heapq.nlargest(k, nums)[-1]

    # using quick sort, beats 97%
    def findKthLargest2(self, nums, k):
        return sorted(nums, reverse=True)[k-1]

    def findKthLargest3(self, nums, k):
        heap_list = list()
        for n in nums:
            heapq.heappush(heap_list, -n)
        ans = 0
        for i in range(k):
            ans = -heapq.heappop(heap_list)
        return ans


ques = [[[3, 2, 1, 5, 6, 4], 2], [[3, 2, 3, 1, 2, 4, 5, 5, 6], 4]]

for q in ques:
    s = Solution().findKthLargest3(q[0], q[1])
    print(s)
