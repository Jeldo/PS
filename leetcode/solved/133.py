# Definition for a Node.
from collections import defaultdict


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors: list[Node] = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        visited = set()
        graph = defaultdict(list)

        def dfs(node):
            if node.val in visited:
                return
            if not node.neighbors:
                return

            visited.add(node.val)
            for neighbor in node.neighbors:
                graph[node.val].append(neighbor.val)
                dfs(neighbor)

        dfs(node)

        new_node = Node(1)
        nodes = defaultdict(Node)
        nodes[1] = new_node
        for key, neighbors in graph.items():
            for n in neighbors:
                if n not in nodes:
                    nodes[n] = Node(n)
                nodes[key].neighbors.append(nodes[n])

        return new_node


cases = []

node_1 = Node(1)
node_2 = Node(2)
node_3 = Node(3)
node_4 = Node(4)
node_1.neighbors.extend([node_2, node_4])
node_2.neighbors.extend([node_1, node_3])
node_3.neighbors.extend([node_2, node_4])
node_4.neighbors.extend([node_1, node_3])
cases.append(node_1)

node_1 = Node(1)
cases.append(node_1)

node_1 = Node(1)
node_2 = Node(2)
node_1.neighbors.append(node_2)
node_2.neighbors.append(node_1)
cases.append(node_1)

for c in cases:
    print(Solution().cloneGraph(c))
