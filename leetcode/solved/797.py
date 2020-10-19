'''
Backtracking, DFS, Graph
'''


class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        result = []

        def dfs(n: int, path: list[int]):
            nonlocal graph, result
            if n == len(graph) - 1:
                result.append(path + [n])
                return
            if not graph[n]:
                return
            for i in graph[n]:
                dfs(i, path + [n])

        dfs(0, [])
        return result


cases = [
    [[1, 2], [3], [3], []],
    [[4, 3, 1], [3, 2, 4], [3], [4], []],
    [[1], []],
    [[1, 2, 3], [2], [3], []],
    [[1, 3], [2], [3], []]
]

for c in cases:
    s = Solution().allPathsSourceTarget(c)
    print(s)
