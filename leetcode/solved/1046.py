'''
Time Complexity: O(nlogn) due to heap queue
'''
import heapq


class Solution:
    def lastStoneWeight(self, stones):
        stone_heap = [-x for x in stones]
        heapq.heapify(stone_heap)
        while len(stone_heap) > 1:
            y = heapq.heappop(stone_heap) * -1
            x = heapq.heappop(stone_heap) * -1
            if x < y:
                next_stone = (y-x) * -1
                heapq.heappush(stone_heap, next_stone)
        return stone_heap[0]*-1 if stone_heap else 0


stones = [2, 7, 4, 1, 8, 1]
s = Solution().lastStoneWeight(stones)
print(s)
