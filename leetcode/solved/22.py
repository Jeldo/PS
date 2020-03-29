class Solution:
    # def generateParenthesis(self, n):
    #     parenthesis = list()

    #     def dfs(cur_parentheses: str, stack: list):
    #         # print('{}\t\t\t\t{}'.format(cur_parentheses, stack))
    #         if len(cur_parentheses) == n*2 and len(stack) == 0:
    #             parenthesis.append(cur_parentheses)
    #         else:
    #             if cur_parentheses.count('(') < n:
    #                 stack.append('(')
    #                 dfs(cur_parentheses + '(', stack)
    #             if cur_parentheses.count(')') < n and cur_parentheses.count(')') < cur_parentheses.count('('):
    #                 if len(stack) > 0 and stack[-1] == '(':
    #                     stack.pop()
    #                 dfs(cur_parentheses + ')', stack)
    #     dfs('(', ['('])
    #     return parenthesis

    def generateParenthesis(self, n):
        parenthesis = list()

        def dfs(cur_parenthesis, open_p, close_p):
            if len(cur_parenthesis) == n * 2:
                parenthesis.append(cur_parenthesis)
                return
            if open_p < n:
                dfs(cur_parenthesis+'(', open_p+1, close_p)
            if close_p < open_p:
                dfs(cur_parenthesis+')', open_p, close_p+1)
        dfs('', 0, 0)
        return parenthesis


n = 3

s = Solution().generateParenthesis(n)
print(s)
