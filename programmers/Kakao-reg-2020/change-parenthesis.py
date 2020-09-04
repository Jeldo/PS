def solution(p):
    def validate(s):
        stack = 0
        for p in s:
            if p == '(':
                stack += 1
            else:
                stack -= 1
            if stack < 0:
                return False
        return True

    def recursive(w):
        if len(w) == 0:
            return ''
        bal = 0
        u = v = ''
        for i in range(len(w)):
            bal = bal - 1 if w[i] == '(' else bal + 1
            if bal == 0:
                u = w[:i+1]
                v = w[i+1:]
                if validate(u):
                    return u + recursive(v)
                else:
                    temp = '(' + recursive(v) + ')'
                    for p in u[1:-1]:
                        if p == '(':
                            temp += ')'
                        else:
                            temp += '('
                    return temp
    return recursive(p)


cases = [
    "(()())()",
    ")(",
    "()))((()"
]

for c in cases:
    s = solution(c)
    print(s)
