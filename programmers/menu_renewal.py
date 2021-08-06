from collections import Counter

from itertools import combinations


def solution(orders, course):
    answer = []
    for c in course:
        menus = []
        for order in orders:
            combination = combinations(sorted(order), c)
            menus += combination
        counter = Counter(menus)

        if counter:
            max_frequent_menu = max(counter.values())
            if max_frequent_menu > 1:
                for k, v in counter.items():
                    if v == max_frequent_menu:
                        answer.append(''.join(k))
    answer.sort()
    return answer


cases = [
    [["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]],
    [["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]],
    [["XYZ", "XWY", "WXA"], [2, 3, 4]],
]
for case in cases:
    print(solution(*case))
