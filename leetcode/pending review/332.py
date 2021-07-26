from collections import defaultdict, deque


class Solution:
    def findItinerary(self, tickets: list[list[str]]) -> list[str]:
        result = []
        tickets.sort()
        graph = defaultdict(deque)
        for s, d in tickets:
            graph[s].append(d)

        def dfs(path):
            while graph[path]:
                next_path = graph[path].popleft()
                dfs(next_path)
            result.append(path)

        dfs('JFK')
        return result[::-1]


cases = [
    [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
    [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]],
]

for c in cases:
    print(Solution().findItinerary(c))
