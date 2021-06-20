<<<<<<< HEAD
# O(N*M)
def solution(S, P, Q):
    result = []
    for p, q in zip(P, Q):  # O(N)
        subsequence = S[p:q+1]
        if 'A' in subsequence:  # O(M)
            result.append(1)
        elif 'C' in subsequence:
            result.append(2)
        elif 'G' in subsequence:
            result.append(3)
        elif 'T' in subsequence:
            result.append(4)
    return result


cases = [
    ['CAGCCTA', [2, 5, 0], [4, 5, 6]]
=======
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
>>>>>>> 3553b9b... codility
]

for c in cases:
    res = solution(*c)
    print(res)
