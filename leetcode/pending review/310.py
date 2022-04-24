class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(set)
        for e in edges:
            graph[e[0]].add(e[1])
            graph[e[1]].add(e[0])

        leaves = set()
        for node, values in graph.items():
            if len(values) == 1:
                leaves.add(node)

        while n > 2:
            n -= len(leaves)
            new_leaves = set()
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)

                if len(graph[neighbor]) == 1:
                    new_leaves.add(neighbor)

            leaves = new_leaves

        return list(leaves)
