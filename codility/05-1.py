def solution(A, B, K):
    x = B // K - A // K
    return x if A % K != 0 else x + 1


cases = [
    [6, 11, 2],
    [0, 1, 11],
    [0, 0, 11],
    [10, 10, 5]
]

for c in cases:
    res = solution(*c)
    print(res)
