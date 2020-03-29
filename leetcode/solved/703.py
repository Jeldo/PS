'''
using min-heap
'''
import heapq


class KthLargest:

    # O(nlogn)
    def __init__(self, k, nums):
        self.k = k
        self.heap_nums = sorted(nums, reverse=True)[:k]
        heapq.heapify(self.heap_nums)

    # O(logn)
    def add(self, val):
        if len(self.heap_nums) < self.k:
            heapq.heappush(self.heap_nums, val)
        elif val > self.heap_nums[0]:
            heapq.heappushpop(self.heap_nums, val)
        return self.heap_nums[0]


k = 2
nums = [0]
kl = KthLargest(k, nums)
print(kl.add(-1))
print(kl.add(1))
print(kl.add(-2))
print(kl.add(-4))
print(kl.add(3))
