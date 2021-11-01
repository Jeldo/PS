from collections import defaultdict
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = set()

        def dfs(node):
            total_cost = 0
            visited.add(node)
            for n in graph[node]:
                if n in visited:
                    continue
                cost = dfs(n)
                if cost or hasApple[n]:
                    total_cost += cost + 2

            return total_cost

        return dfs(0)

    def minTime1(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for e in edges:
            u, v = e
            graph[u].append(v)

        def dfs(node):
            apples = 0

            for n in graph[node]:
                apples += dfs(n)
            if apples or hasApple[node]:
                return apples + 1
            return apples

        total_apples = dfs(0)
        if total_apples:
            return (total_apples - 1) * 2
        return 0


cases = [
    [7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [False, False, True, False, True, True, False]],
    [7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [False, False, True, False, False, True, False]],
    [7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [False, False, False, False, False, False, False]],
    [4, [[0, 2], [0, 3], [1, 2]], [False, True, False, False]],
]

for c in cases:
    print(Solution().minTime(*c))
