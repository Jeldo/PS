'''
using max-heap

heapq with multiple elements
https://stackoverflow.com/questions/3954530/how-to-make-heapq-evaluate-the-heap-off-of-a-specific-attribute
'''
import heapq


class Solution:
    def kClosest(self, points, K):
        point_heap = list()
        farthest = 0
        for p in points:
            distance = p[0]**2+p[1]**2
            if len(point_heap) < K:
                heapq.heappush(point_heap, (-distance, (p[0], p[1])))
                if farthest > distance:
                    farthest = distance
            elif farthest < distance:
                heapq.heappushpop(
                    point_heap, (-distance, (p[0], p[1])))
        return [p[1] for p in point_heap]


# points = [[3, 3], [5, -1], [-2, 4]]
# K = 2
points = [[1, 3], [-2, 2]]
K = 1
s = Solution().kClosest(points, K)
print(s)
