import heapq


def solution(N, stages):
    d = dict()
    failure_rate = []
    for i in range(1, N+1):
        d[i] = [0, 0]
    for s in stages:
        if s == N + 1:
            continue
        if s not in d:
            d[s] = [1, 0]
        else:
            d[s][0] += 1
    total = len(stages)
    for k, v in d.items():
        if total <= 0:
            d[k][1] = 0
        else:
            d[k][1] = d[k][0] / total
        total -= d[k][0]
        failure_rate.append((-d[k][1], k))
    res = heapq.nsmallest(N, failure_rate)
    return [x[1] for x in res]


cases = [
    [5, [2, 1, 2, 6, 2, 4, 3, 3]],
    [4, [4, 4, 4, 4, 4]],
    [3, [2, 2, 2]]
]

for c in cases:
    s = solution(*c)
    print(s)
