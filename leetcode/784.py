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

    def letterCasePermutation2(self, S: str):
        result = set()

        def dfs(converted, i):
            if converted not in result:
                if converted:
                    result.add(converted)
            if i >= len(converted):
                return
            if converted[i].isalpha():
                dfs(converted[:i]+converted[i].lower() +
                    converted[i+1:], i+1)
                dfs(converted[:i]+converted[i].upper() +
                    converted[i+1:], i+1)
            else:
                dfs(converted, i+1)
        dfs(S, 0)
        return result


S = "a1b2"
s = Solution().letterCasePermutation(S)
print(s)
