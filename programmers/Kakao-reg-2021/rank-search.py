import bisect
from collections import defaultdict


def solution(info: list[str], query: list[str]):
    db = defaultdict(list)
    for data in info:
        for i in range(16):
            binary = bin(i)[2:]
            binary = '0' * (4 - len(binary)) + binary
            data_split = data.split()
            temp = []
            for bit, d in zip(binary, data_split):
                if bit == '0':
                    temp.append('-')
                else:
                    temp.append(d)
            db[tuple(temp)].append(int(data_split[-1]))

    for data in db.values():
        data.sort()

    result = []
    for q in query:
        q = q.split(' and ')
        last_data, target_score = q[-1].split()
        q = tuple(q[:-1] + [last_data])
        position = bisect.bisect_left(db[q], int(target_score))
        result.append(len(db[q]) - position)
    return result


def solution2(info: list[str], query: list[str]):
    result = []
    data = []
    for i in info:
        res = i.split()
        data.append(res[:-1] + [int(res[-1])])
    for q in query:
        count = 0
        q = q.replace('and', '').split()
        for d in data:
            if q[0] == d[0] or q[0] == '-':
                if q[1] == d[1] or q[1] == '-':
                    if q[2] == d[2] or q[2] == '-':
                        if q[3] == d[3] or q[3] == '-':
                            if int(q[4]) <= d[4]:
                                count += 1
        result.append(count)
    return result


cases = [
    # [1,1,1,1,2,4]
    [
        ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
         "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
        ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
         "- and - and - and - 150"],
    ]
]

for c in cases:
    print(solution(*c))
