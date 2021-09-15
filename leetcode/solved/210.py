from collections import defaultdict, deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        indegree = defaultdict(int)

        for p in prerequisites:
            v, u = p
            graph[u].add(v)
            if u in graph[v]:
                return []
            indegree[v] += 1

        s = deque([n for n in range(numCourses) if n not in indegree])
        visited = []
        while s:
            u = s.popleft()
            visited.append(u)
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    s.append(v)

        if len(visited) != numCourses:
            return []
        return visited


cases = [
    [2, [[1, 0]]],
    [2, [[1, 0], [0, 1]]],
    [8, [[3, 0], [3, 1], [4, 1], [4, 2], [5, 3], [6, 3], [6, 4], [7, 3]]],
    [20, [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]],
    [3, [[1, 0], [0, 2], [2, 1]]],
]

for c in cases:
    print(Solution().findOrder(*c))
