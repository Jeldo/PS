from collections import defaultdict


class Solution:
    def minReorder(self, n: int, connections: list):
        count = 0
        roads = set()
        graph = defaultdict(list)
        for u, v in connections:
            roads.add((u, v))
            graph[v].append(u)
            graph[u].append(v)

        def dfs(u, parent):
            nonlocal count
            count += (parent, u) in roads
            for v in graph[u]:
                if v == parent:
                    continue
                dfs(v, u)
        dfs(0, -1)
        return count


cases = [
    [6,  [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]],
    [5, [[1, 0], [1, 2], [3, 2], [3, 4]]]
]

for c in cases:
    s = Solution().minReorder(c[0], c[1])
    print(s)
