# Definition for a Node.
from collections import defaultdict


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors: list[Node] = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, head: Node) -> Node:
        if not head:
            return None

        visited = set()
        graph = defaultdict(list)

        def dfs(node: Node):
            if node.val in visited:
                return
            if not node.neighbors:
                return
            visited.add(node.val)
            for neighbor in node.neighbors:
                graph[node.val].append(neighbor.val)
                dfs(neighbor)

        dfs(head)

        new_head = Node(1)
        nodes = defaultdict(Node)
        nodes[1] = new_head
        for key, values in graph.items():
            for v in values:
                if v not in nodes:
                    nodes[v] = Node(v)
                nodes[key].neighbors.append(nodes[v])

        return new_head


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
