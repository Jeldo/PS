'''
Category: String
'''


class Solution:
    def generateParenthesis(self, n: int):
        answer = []

        def dfs(p, opened, closed):
            nonlocal answer
            if len(p) == n * 2:
                answer.append(p)
                return
            if opened < n:
                dfs(p+'(', opened + 1, closed)
            if opened > closed:
                dfs(p+')', opened, closed + 1)
        dfs('', 0, 0)
        return answer


cases = [
    3, 4
]

for c in cases:
    s = Solution().generateParenthesis(c)
    print(s)
