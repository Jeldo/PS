def solution(s):
    s = s.split()
    if len(s) != 6:
        print(False)
    prev = 0
    state = True
    for n in s:
        n = int(n)
        if not(1 <= n <= 45):
            state = False
            break
        if prev >= n:
            state = False
            break
        prev = n
    print(state)


cases = [
    '1 2 3 4 5 6',
    '1 3 5 7 7 9',
    '1 2 4 5 6',
    '2 1 3 5 7 9',
    '46 1 3 5 7 9'
]

for c in cases:
    solution(c)
