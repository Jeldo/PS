# O(NlogN)
def solution(A):
    if len(A) < 3:
        return 0
    edge = sorted(A, reverse=True)
    for i in range(len(edge)-2):
        if edge[i] < edge[i+1] + edge[i+2]:
            return 1
    return 0


cases = [
    [10, 2, 5, 1, 8, 20],   # 1
    [10, 50, 5, 1],          # 0
    [],
    [1],
    [1, 2],
    [-1, -2, -3],
]

for c in cases:
    res = solution(c)
    print(res)
