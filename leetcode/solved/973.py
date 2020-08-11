'''
Category: heap
heapq with multiple elements
https://stackoverflow.com/questions/3954530/how-to-make-heapq-evaluate-the-heap-off-of-a-specific-attribute
'''
import heapq


class Solution:
    def kClosest(self, points: list, K: int):
        p, res = [], []
        for point in points:
            heapq.heappush(p, (point[0]**2 + point[1]**2, point))
        for _ in range(K):
            res.append(heapq.heappop(p)[1])
        # res = [x[1] for x in heapq.nsmallest(K, p)]
        return res

    def kClosest1(self, points, K):
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


cases = [
    [[[1, 3], [-2, 2]], 1],
    [[[3, 3], [5, -1], [-2, 4]], 2]
]

for c in cases:
    s = Solution().kClosest(c[0], c[1])
    print(s)
