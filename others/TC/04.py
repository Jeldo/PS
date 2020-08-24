from queue import deque


def solution(c):

    banks = c.split()
    q = deque()
    for b in banks:
        if not q:
            q.appendleft(b)
        if b not in q:
            q.appendleft(b)
        else:
            q.remove(b)
            q.appendleft(b)
        if len(q) > 5:
            q.pop()
        print(' '.join(list(q)))


cases = [
    '우리 우리 우리 하나 우리 국민 삼성 농협 농협 농협 국민 저축'
]

for c in cases:
    solution(c)
