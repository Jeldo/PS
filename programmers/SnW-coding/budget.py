def solution(d, budget):
    count = 0
    for dept in sorted(d):
        if 0 <= budget - dept:
            budget -= dept
            count += 1
    return count


cases = [
    ([1, 3, 2, 5, 4], 9),
    ([2, 2, 3, 3], 10)
]

for c in cases:
    s = solution(c[0], c[1])
    print(s)
