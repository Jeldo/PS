import heapq
from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(dict[int])
        for u, v, w in flights:
            graph[u][v] = w
        q = [(0, src, k)]
        distance = {i: (float('inf'), k) for i in range(n)}
        distance[src] = (0, 2)

        while q:
            price, u, step = heapq.heappop(q)
            if u == dst:
                return price
            if step >= 0:
                for v in graph[u]:
                    p = price + graph[u][v]
                    d, s = distance[v]
                    if p < d or step - 1 >= s:
                        distance[v] = (p, step - 1)
                        heapq.heappush(q, (p, v, step - 1))
        return -1


cases = [
    [3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1],
    [3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0],
    [5, [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]], 0, 2, 2],
]

for c in cases:
    print(Solution().findCheapestPrice(*c))
