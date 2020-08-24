def solution(citations):
    answer = 0
    citations = sorted(citations, reverse=True)
    print(citations)
    for i, c in enumerate(citations):
        if i + 1 <= c:
            answer = i + 1
        else:
            break
    return answer


cases = [
    [3, 0, 6, 1, 5],
    [3, 0, 6, 1, 5, 4, 3],
    [3, 0, 6, 4, 5],
    [6, 5, 2, 1, 0],
    [3, 30, 34, 5, 9]
]

for c in cases:
    s = solution(c)
    print(s)
