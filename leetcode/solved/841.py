'''
Category: DFS
'''


class Solution:
    def canVisitAllRooms(self, rooms: list):
        visited = [False] * len(rooms)

        def dfs(room_number):
            nonlocal visited
            visited[room_number] = True
            for i in rooms[room_number]:
                if not visited[i]:
                    dfs(i)
        dfs(0)
        return all(visited)


cases = [
    [[1], [2], [3], []],
    [[1, 3], [3, 0, 1], [2], [0]]
]

for c in cases:
    s = Solution().canVisitAllRooms(c)
    print(s)
