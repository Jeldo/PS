class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        found_words = set()

        def dfs(word, index, r, c, visited):
            if not (0 <= r < len(board) and 0 <= c < len(board[0])):
                return
            if visited[r][c]:
                return

            visited[r][c] = True
            if index == len(word) - 1 and word[index] == board[r][c]:
                found_words.add(word)
                return
            if word[index] == board[r][c]:
                for dr, dc in directions:
                    dfs(word, index + 1, r + dr, c + dc, visited)
            visited[r][c] = False

        for word in words:
            visited = [[False] * len(board[0]) for _ in range(len(board))]
            for i in range(len(board)):
                for j in range(len(board[0])):
                    dfs(word, 0, i, j, visited)

        return list(found_words)


cases = [
    [[["o", "a", "a", "n"], ["e", "t", "a", "e"], ["i", "h", "k", "r"], ["i", "f", "l", "v"]],
     ["oath", "pea", "eat", "rain"]],
    [[["a", "b"], ["c", "d"]], ["abcd"]],
    [[["o", "a", "b", "n"], ["o", "t", "a", "e"], ["a", "h", "k", "r"], ["a", "f", "l", "v"]], ["oa", "oaa"]],
    [[["a", "a"]], ["aaa"]],
    [[["a", "b", "c", "e"], ["x", "x", "c", "d"], ["x", "x", "b", "a"]], ["abc", "abcd"]],
    [[["x", "a", "x"], ["b", "b", "x"], ["x", "c", "x"]], ["abc", "bbc"]],
]

for case in cases:
    print(Solution().findWords(*case))
