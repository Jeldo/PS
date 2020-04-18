from collections import defaultdict


def show_graph(graph):
    for i in range(0, len(graph)):
        for j in range(0, len(graph[0])):
            print(graph[i][j], end=' ')
        print()
    print()


class Solution:
    def regionsBySlashes(self, grid: list):
        l = len(grid) + 1
        graph = defaultdict(list)
        regions = 0

        def add_edge(u, v):
            nonlocal graph
            graph[u].append(v)

        def find_parent(parent, vt):
            r, c = vt[0], vt[1]
            if not parent[r][c]:
                return vt
            if parent[r][c]:
                return find_parent(parent, parent[r][c])

        def union(parent, vx, vy):
            x_set = find_parent(parent, vx)
            y_set = find_parent(parent, vy)
            xr, xc = x_set[0], x_set[1]
            yr, yc = y_set[0], y_set[1]
            parent[xr][xc] = y_set

        def is_cyclic():
            nonlocal regions
            parent = [[None] * (l) for _ in range(l)]
            for vi in graph:
                is_last = False
                for vj in graph[vi]:
                    x = find_parent(parent, vi)
                    y = find_parent(parent, vj)
                    if x == y:
                        regions += 1
                        break
                        # return True
                    union(parent, x, y)

        for i in range(0, l-1):
            for j in range(0, l-1):
                if grid[i][j] == '/':
                    add_edge((i, j+1), (i+1, j))
                elif grid[i][j] == '\\':
                    add_edge((i, j), (i+1, j+1))

        for i in range(0, l-1):
            # add horizontal edges
            add_edge((0, i), (0, i+1))
            add_edge((l-1, i), (l-1, i+1))
            # add vertical edges
            add_edge((i, 0), (i+1, 0))
            add_edge((i, l-1), (i+1, l-1))

        is_cyclic()
        print(graph)
        return regions

        # l = len(grid)
        # graph = [[False] * (l + 1) for _ in range(l + 1)]
        # graph[0][0], graph[0][l], graph[l][0], graph[l][l] = True, True, True, True
        # for i in range(0, l):
        #     for j in range(0, l):
        #         if grid[i][j] == '/':
        #             graph[i+1][j] = True
        #             graph[i][j+1] = True
        #         elif grid[i][j] == '\\':
        #             graph[i][j] = True
        #             graph[i+1][j+1] = True
        # show_graph(graph)
        # return


# 2 1 4 5 3

cases = [
    [
        " /",
        "/ "
    ],
    [
        " /",
        "  "
    ],
    [
        "\\/",
        "/\\"
    ], [
        "/\\",
        "\\/"
    ],
    [
        "//",
        "/ "
    ]
]

for c in cases:
    s = Solution().regionsBySlashes(c)
    print(s)
