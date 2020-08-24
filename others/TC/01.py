def solution(s):
    prev = s[0]
    i = 1
    state = True
    while i < len(s):
        cur = s[i]
        if not (cur != '1' or cur != '2'):
            state = False
            break
        elif prev == '1':
            if not cur == '2':
                state = False
                break
        prev = cur
        i += 1
    if s[i-1] == '1':
        state = False
    print(state)


cases = [
    '11',
    '12',
    '121',
    '122'
]

for c in cases:
    solution(c)
