def solution(X, Y, D):
    distance = Y-X
    if distance == 0:
        return 0
    q, r = divmod(distance, D)
    answer = 0
    if q > 0:
        answer += q
    if r > 0:
        answer += 1
    return answer


cases = [
    [10, 85, 30],
    [10, 100, 30],
    [10, 110, 30],
]

for c in cases:
    res = solution(*c)
    print(res)
