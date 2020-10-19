from itertools import combinations


def solution(relation):
    answer = 0
    attribute = [set() for _ in range(len(relation[0]))]
    unique, rest = [], []
    for i in range(len(attribute)):
        is_unique = True
        for r in relation:
            if r[i] not in attribute[i]:
                attribute[i].add(r[i])
            else:
                is_unique = False
                break
        if is_unique:
            unique.append(i)
        else:
            rest.append(i)
    print(unique, rest)
    for i in range(2, len(rest)+1):
        for x in combinations(rest, i):
            print(x)
    return answer


cases = [
    [
        ["100", "ryan", "music", "2"],
        ["200", "apeach", "math", "2"],
        ["300", "tube", "computer", "3"],
        ["400", "con", "computer", "4"],
        ["500", "muzi", "music", "3"],
        ["600", "apeach", "music", "2"]
    ]
]

for c in cases:
    s = solution(c)
    print(s)
