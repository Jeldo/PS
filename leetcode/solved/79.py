class Solution:
    # O(n*m)
    def exist(self, board: list[list[str]], word: str) -> bool:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        result = False

        def dfs(i, j, visited, w):
            nonlocal result
            if (i, j) in visited:
                return
            if not (0 <= i < len(board)) or not (0 <= j < len(board[0])):
                return
            w += board[i][j]
            if not (word[:len(w)] == w):
                return
            visited.add((i, j))
            if w == word:
                result = True
                return
            for d in dirs:
                dfs(i + d[0], j + d[1], visited, w)
            visited.remove((i, j))

        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(i, j, set(), "")
                if result:
                    return True
        return False


cases = [
    [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"],
    [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"],
    [[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"]
]

for c in cases:
    print(Solution().exist(*c))
