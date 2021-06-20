# O(S)
def solution(S):
    bracket = {'(': ')', '{': '}', '[': ']'}
    stack = []
    for ch in S:
        if ch in bracket:
            stack.append(bracket[ch])
        else:
            if not stack:
                return 0
            if ch != stack[-1]:
                return 0
            if ch == stack[-1]:
                stack.pop()
    return 1 if not stack else 0


cases = [
    '{[()()]}',
    ']]])))',
    '([)]',
    ')(',
    '()(',
    '())',
    '([{}])'
]

for c in cases:
    res = solution(c)
    print(res)
