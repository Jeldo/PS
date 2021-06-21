# O(N*M)
def solution(S, P, Q):
    result = []
    for p, q in zip(P, Q):  # O(N)
        subsequence = S[p:q + 1]
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
    ['CAGCCTA', [2, 5, 0], [4, 5, 6]],
]

for c in cases:
    res = solution(*c)
    print(res)
