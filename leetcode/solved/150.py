# O(n)
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def is_digit(token: str):
            return token.lstrip('-').isnumeric()

        def op(token, n1, n2):
            if token == '+':
                return n1 + n2
            elif token == '-':
                return n1 - n2
            elif token == '*':
                return n1 * n2
            else:
                return int(n1 / n2)

        stack = []
        for token in tokens:
            if is_digit(token):
                stack.append(int(token))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                res = op(token, n1, n2)
                stack.append(res)
        return stack[-1]
