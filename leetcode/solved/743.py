import heapq
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(dict[int])
        for u, v, w in times:
            graph[u][v] = w
        distances = {i: float('inf') for i in range(1, n + 1)}
        distances[k] = 0
        visited = set()
        q = [(0, k)]

        while q:
            w, u = heapq.heappop(q)
            if u not in visited:
                visited.add(u)
                for v in graph[u]:
                    if v not in visited:
                        if distances[v] > graph[u][v] + w:
                            distances[v] = graph[u][v] + w
                            heapq.heappush(q, (distances[v], v))

        if len(visited) != n:
            return -1
        return max(distances.values())


cases = [
    [[[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2],
    [[[1, 2, 1]], 2, 1],
    [[[1, 2, 1]], 2, 2],
    [[[1, 2, 1], [2, 1, 3]], 2, 2],
    [[[1, 2, 1], [1, 5, 1], [2, 3, 2], [2, 4, 1], [3, 5, 2], [4, 5, 1], [6, 7, 1], [8, 7, 1]], 8, 1],  # -1
    [[[1, 2, 1], [2, 2, 3], [2, 3, 2]], 3, 1],
]

for case in cases:
    print(Solution().networkDelayTime(*case))
