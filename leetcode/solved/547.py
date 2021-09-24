from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = dict()
        for i, connected in enumerate(isConnected):
            graph[i] = list()
            for j in range(len(connected)):
                if connected[j] == 1:
                    graph[i].append(j)

        def dfs(city: int):
            while graph[city]:
                next_city = graph[city].pop()
                dfs(next_city)

        province = 0

        for city in range(len(isConnected)):
            if graph[city]:
                dfs(city)
                province += 1

        return province


cases = [
    [[1, 1, 0], [1, 1, 0], [0, 0, 1]],  # 2
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]],  # 3
    [
        [1, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0],
        [0, 1, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 1],
    ],  # 2
]

for c in cases:
    print(Solution().findCircleNum(c))
