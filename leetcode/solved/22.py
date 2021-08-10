class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        parenthesis = []

        def dfs(p, l, r):
            if len(p) == 2 * n and l == r:
                parenthesis.append(p)
                return
            if l < r or n < l or n < r:
                return
            dfs(p + '(', l + 1, r)
            dfs(p + ')', l, r + 1)

        dfs('', 0, 0)
        return parenthesis


cases = [
    3, 4
]

for c in cases:
    print(Solution().generateParenthesis(c))
