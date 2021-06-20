def solution(S, P, Q):
    DNA = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    min_impact = []
    for p, q in zip(P, Q):
        min_sequence = DNA[S[p]]
        for i in range(p, q+1):
            min_sequence = min(min_sequence, DNA[S[i]])
        min_impact.append(min_sequence)
    return min_impact


cases = [
    ['CAGCCTA', [2, 5, 0], [4, 5, 6]],
]

for c in cases:
    res = solution(*c)
    print(res)
