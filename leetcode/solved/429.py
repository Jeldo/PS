'''
Category: Tree, BFS
Time Complexity:
Space Complexity:
'''

from queue import Queue, deque
from collections import defaultdict


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = list()


def showNodes(node: Node):
    q = Queue()
    q.put(node)
    while not q.empty():
        cur = q.get()
        print(cur.val, end=' ')
        for c in cur.children:
            q.put(c)
    print()


class Solution:
    def levelOrder(self, root: Node):
        def bfs(node: Node):
            nodes = list()
            q = deque()
            q.append(node)
            while q:
                temp_list = list()
                temp_q = deque()
                for parent in q:
                    if parent:
                        temp_list.append(parent.val)
                        for child in parent.children:
                            temp_q.append(child)
                q = temp_q
                if temp_list:
                    nodes.append(temp_list)
            return nodes

        # showNodes(root)
        def bfs1(node: Node):
            if not node:
                return []
            q1 = Queue()
            q2 = Queue()
            q1.put(node)
            nodes = list([[node.val]])
            same_level_nodes = list()
            while not q1.empty():
                cur = q1.get()
                for c in cur.children:
                    q2.put(c)
                    same_level_nodes.append(c.val)
                if q1.empty():
                    if same_level_nodes:
                        nodes.append(same_level_nodes)
                        same_level_nodes = list()
                    q1 = q2
                    q2 = Queue()
            return nodes

        def bfs2(node: Node):
            if not node:
                return []
            q1 = list([node])
            q2 = list()
            nodes = list([[node.val]])
            same_level_nodes = list()
            while q1:
                cur = q1.pop(0)
                for c in cur.children:
                    q2.append(c)
                    same_level_nodes.append(c.val)
                if len(q1) == 0:
                    if same_level_nodes:
                        nodes.append(same_level_nodes)
                        same_level_nodes = list()
                    q1 = q2
                    q2 = list()
            return nodes

        def bfs3(node: Node):
            if not node:
                return []
            q1 = Queue()
            q1.put((node, 0))
            d = defaultdict(list)
            while not q1.empty():
                cur, level = q1.get()
                d[level].append(cur.val)
                for c in cur.children:
                    q1.put((c, level + 1))
            return [v for k, v in d.items()]

        def bfs4(node: Node):
            if not node:
                return []
            q1 = Queue()
            q1.put(node)
            nodes = list()
            same_level_nodes = list()
            parent_count, children_count = 1, 0

            while not q1.empty():
                cur = q1.get()
                parent_count -= 1
                children_count += len(cur.children)
                same_level_nodes.append(cur.val)
                if parent_count == 0:
                    nodes.append(same_level_nodes)
                    same_level_nodes = list()
                    parent_count = children_count
                    children_count = 0
                for c in cur.children:
                    q1.put(c)
            return nodes

        return bfs(root)


cases = list()

head = Node(1)
c = Node(3)
c.children.append(Node(5))
c.children.append(Node(6))
head.children.append(c)
head.children.append(Node(2))
head.children.append(Node(4))
cases.append(head)


four = Node(4)
eight = Node(8)
eight.children.append(Node(12))
four.children.append(eight)

five = Node(5)
nine = Node(9)
nine.children.append(Node(13))
ten = Node(10)
five.children.extend([nine, ten])


two = Node(2)
three = Node(3)
elev = Node(11)
elev.children.append(Node(14))
seven = Node(7)
seven.children.append(elev)
three.children.extend([Node(6), seven])

one = Node(1)
one.children.extend([two, three, four, five])
cases.append(one)

for c in cases:
    s = Solution().levelOrder(c)
    print(s)
