from collections import defaultdict


def solution(c):
    nums = c.split()
    d = dict()
    for n in nums:
        n = int(n)
        if n not in d:
            print(n)
            d[n] = n
        else:
            print(d[n])

    print(d)


cases = [
    '1 1 3 4 3 6 3'
]

for c in cases:
    solution(c)
