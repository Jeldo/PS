'''
Category: Tree, BFS
Time Complexity:
Space Complexity:
'''

from queue import Queue


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
        # showNodes(root)

        def bfs(node: Node):
            q = Queue()
            q.put(node)
            nodes = list([[node.val]])
            while not q.empty():
                n = list()
                cur = q.get()
                for c in cur.children:
                    q.put(c)
                    n.append(c.val)
                if n:
                    nodes.append(n)
            return nodes

        def bfs2(node: Node):
            q = list()
            q.append(node)
            nodes = list()
            n = list()
            last = node.val
            while q:
                cur = q.pop(0)
                for c in cur.children:
                    q.append(c)
                    n.append(c.val)
                    print(cur.val, last)
                    if cur.val == last:
                        print('ok')
                        last = c.val
                        nodes.append(n)
                        n.clear()

                # print([x.val for x in q])
                # if n:
                #     nodes.append(n)
            return nodes
        return bfs2(root)


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
    print('----------')
