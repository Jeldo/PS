def solution(w, h):
    def gcd(a, b):
        while b != 0:
            n = a % b
            a = b
            b = n
        return a
    return w * h - (w + h - gcd(max(w, h), min(w, h)))


cases = [
    (8, 12),
    (4, 4),
]


for c in cases:
    s = solution(c[0], c[1])
    print(s)
