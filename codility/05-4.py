# O(N)
def solution(A):
    sub_array = []
    total = 0
    threshold = 1000000000
    for i in range(len(A)):
        if A[i] == 0:
            sub_array = A[i:]
            break
    count = sub_array.count(1)
    for i in range(len(sub_array)):
        if sub_array[i] == 1:
            count -= 1
        elif sub_array[i] == 0:
            total += count
        if threshold < total:
            break
    return total if total <= threshold else -1


cases = [
    [0, 1, 0, 1, 1],
    [1],
    [0],
    [0, 1],
    [1, 0],
    [1, 1, 1, 1, 0]
]

for c in cases:
    res = solution(c)
    print(res)
