'''
Backtracking
'''


class Solution:
    def letterCasePermutation(self, S: str):

        def dfs(converted, i):
            if len(converted) == len(S):
                res.append(converted)
            else:
                if S[i].isalpha():
                    dfs(converted+S[i].swapcase(), i+1)
                dfs(converted+S[i], i+1)
        res = list()
        dfs('', 0)
        return res

    def letterCasePermutation(self, S: str) -> list:
        answers = set()

        def dfs(s: str, i: int):
            if len(s) <= i:
                return
            if s[i].isalpha():
                lower = s[:i]+s[i].lower()+s[i+1:]
                upper = s[:i]+s[i].upper()+s[i+1:]
                answers.add(lower)
                answers.add(upper)
                dfs(lower, i+1)
                dfs(upper, i+1)
            else:
                answers.add(s)
                dfs(s, i+1)

        dfs(S, 0)
        return answers


S = "a1b2"
s = Solution().letterCasePermutation(S)
print(s)
