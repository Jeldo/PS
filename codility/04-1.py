# O(N), N: length of A
def solution(X, A):
    leaves = set(range(1, X+1))
    for i in range(len(A)):
        if A[i] in leaves:
            leaves.remove(A[i])
        if len(leaves) == 0:
            return i
    return -1


cases = [
    [5, [1, 3, 1, 4, 2, 3, 5, 4]],
    [5, [1, 2, 3, 4, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 5]]
]

for c in cases:
    res = solution(*c)
    print(res)
