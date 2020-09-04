from collections import Counter


def solution(str1, str2):
    s1, s2 = '', ''

    def make_dict(str):
        c = Counter()
        for i in range(1, len(str)):
            if str[i].isalpha() and str[i-1].isalpha():
                c[str[i-1:i+1].lower()] += 1
        return c

    pool_s1, pool_s2 = make_dict(str1), make_dict(str2)
    similarity = 1
    if pool_s1 or pool_s2:
        intersection = Counter()
        union = Counter()
        for key in set(pool_s1).intersection(set(pool_s2)):
            intersection[key] = min(pool_s1[key], pool_s2[key])
        for key in set(pool_s1).union(set(pool_s2)):
            union[key] = max(pool_s1[key], pool_s2[key])
        similarity = sum(intersection.values()) / sum(union.values())
    return int(similarity * 65536)


cases = [
    ['FRANCE', 'french'],
    ['handshake', 'shake hands'],
    ['aa1+aa2', 'AAAA12'],
    ['E=M*C^2', 'e=m*c^2'],
]

for c in cases:
    s = solution(*c)
    print(s)
