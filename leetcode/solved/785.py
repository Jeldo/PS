from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        # -1: not colored
        # 0, 1: colors
        colors = [-1] * n

        def dfs(i, color):
            colors[i] = color  # color current node
            for node in graph[i]:  # iterate adjacent nodes
                if colors[node] == color:  # return false if adjacent node color is same as current node's
                    return False
                # return false if not colored adjacent node and
                # the node is not colored in different color
                elif colors[node] == -1 and not dfs(node, 1 - color):
                    return False
            return True

        for i in range(n):
            if colors[i] == -1 and not dfs(i, 0):
                return False
        return True


cases = [
    [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]],
    [[1, 3], [0, 2], [1, 3], [0, 2]],
]

for c in cases:
    print(Solution().isBipartite(c))
