# O(n)
def solution(A):
    check = [False] * len(A)
    for n in A:
        if len(A) < n:
            return 0
        check[n-1] = True
    for i in check:
        if not i:
            return 0
    return 1


cases = [
    [4, 1, 3, 2],
    [1, 2, 4]
]

for c in cases:
    res = solution(c)
    print(res)
