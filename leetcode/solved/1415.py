'''
Backtracking
'''


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        strings = []

        def dfs(s: str):
            if k == len(strings):
                return
            if len(s) == n:
                strings.append(s)
                return
            if s == '':
                dfs('a')
                dfs('b')
                dfs('c')
            else:
                if s[-1] != 'a':
                    dfs(s+'a')
                if s[-1] != 'b':
                    dfs(s+'b')
                if s[-1] != 'c':
                    dfs(s+'c')

        dfs('')
        return strings[k-1] if k <= len(strings) else ''


cases = [
    [1, 3],
    [1, 4],
    [3, 9],
    [2, 7],
    [10, 100]
]

for c in cases:
    s = Solution().getHappyString(*c)
    print(s)
