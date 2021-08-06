from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        traced = set()
        visited = set()
        for p1, p2 in prerequisites:
            graph[p1].append(p2)

        def dfs(i):
            if i in traced:
                return False
            if i in visited:
                return True

            traced.add(i)
            for n in graph[i]:
                if not dfs(n):
                    return False

            # backtrack
            traced.remove(i)
            visited.add(i)
            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True


cases = [
    [2, [[1, 0]]],
    [2, [[1, 0], [0, 1]]],
    [4, [[1, 0], [3, 1], [2, 1]]]
]

for case in cases:
    print(Solution().canFinish(*case))
