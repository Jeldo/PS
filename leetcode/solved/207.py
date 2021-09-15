from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        indegree = defaultdict(int)

        for p in prerequisites:
            v, u = p
            if u in graph[v] or u == v:
                return False
            graph[u].add(v)
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

        return len(visited) == numCourses


cases = [
    [2, [[1, 0]]],
    [2, [[1, 0], [0, 1]]],
    [8, [[3, 0], [3, 1], [4, 1], [4, 2], [5, 3], [6, 3], [6, 4], [7, 3]]],
    [20, [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]],
    [3, [[1, 0], [0, 2], [2, 1]]],
]

for c in cases:
    print(Solution().canFinish(*c))
