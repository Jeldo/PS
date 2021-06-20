# O(NlogN)
def solution(A):
    circles = []
    for i, v in enumerate(A):
        circles.append((i+v, 1))
        circles.append((i-v, -1))
    circles.sort()
    print(circles)

    intersect = 0
    opened = 0
    threshold = 10000000

    for i, v in enumerate(circles):
        if v[1] == 1:
            opened -= 1
        elif v[1] == -1:
            intersect += opened
            opened += 1
        if threshold < intersect:
            break
    return intersect if intersect <= threshold else -1


cases = [
    [1, 5, 2, 1, 4, 0]
]

for c in cases:
    res = solution(c)
    print(res)
