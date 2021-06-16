def solution(A):
    return sum(range(len(A)+2)) - sum(A)


cases = [
    [2, 3, 1, 5],
    [2, 3, 4, 5],
    [],
    [1],
    [1, 3],
]

for c in cases:
    res = solution(c)
    print(res)
