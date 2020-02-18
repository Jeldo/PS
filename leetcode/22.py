class Solution:
    def generateParenthesis(self, n):
        parenthesis = list()

        def dfs(cur_parentheses: str, next_p: str, stack: list):
            cur_parentheses += next_p
            print('{}\t\t\t\t{}'.format(cur_parentheses, stack))
            if len(cur_parentheses) == n*2 and len(stack) == 0:
                parenthesis.append(cur_parentheses)
            else:
                if cur_parentheses.count('(') < n:
                    stack.append('(')
                    dfs(cur_parentheses, '(', stack)
                if cur_parentheses.count(')') < n and cur_parentheses.count(')') < cur_parentheses.count('('):
                    if len(stack) > 0 and stack[-1] == '(':
                        stack.pop()
                    dfs(cur_parentheses, ')', stack)
        p = str()
        stack = ['(']
        dfs(p, '(', stack)
        return parenthesis


n = 4

s = Solution().generateParenthesis(n)
print(s)
