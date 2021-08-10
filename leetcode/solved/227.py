import math


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        op = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in {'+', '-', '*', '/'} or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                elif op == '/':
                    stack.append(math.trunc(stack.pop() / num))
                num = 0
                op = s[i]
        return sum(stack)

    def calculate2(self, s: str) -> int:
        def calc(elements, operator1, operator2):
            stack = []
            for e in elements:
                if stack and (stack[-1] == operator1 or stack[-1] == operator2):
                    op = stack.pop()
                    prev_num = stack.pop()
                    if op == '*':
                        stack.append(prev_num * e)
                    elif op == '/':
                        stack.append(prev_num // e)
                    elif op == '+':
                        stack.append(prev_num + e)
                    elif op == '-':
                        stack.append(prev_num - e)
                else:
                    stack.append(e)
            return stack

        num = ''
        elements = []
        for ch in s:
            if ch.isdigit():
                num += ch
            elif ch != ' ':
                elements.append(int(num))
                num = ''
                elements.append(ch)
        elements.append(int(num))

        multi_div = calc(elements, '*', '/')
        sum_sub = calc(multi_div, '+', '-')
        return sum_sub[0]


cases = [
    "3+2*2",
    " 3/2 ",
    " 3+5 / 2 ",
    "10+22/11+ 3*4 -22",
    "14-3/2",
]

for case in cases:
    print(Solution().calculate(case))
