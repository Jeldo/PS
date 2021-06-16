def solution(A):
    left = A[0]
    right = sum(A[1:])
    diff = abs(left-right)
    for i in range(1, len(A)-1):
        left += A[i]
        right -= A[i]
        diff = min(diff, abs(left-right))
    return diff


cases = [
    [3, 1, 2, 4, 3],
    [2, 5, 6, 3, 10],
]

for c in cases:
    res = solution(c)
    print(res)
