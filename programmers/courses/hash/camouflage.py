from collections import defaultdict


def solution(clothes):
    answer = 1
    d = defaultdict(list)
    for c in clothes:
        d[c[1]].append(c[0])
    for v in d.values():
        answer *= len(v) + 1
    return answer - 1


cases = [
    [
        ['yellow_hat', 'headgear'],
        ['blue_sunglasses', 'eyewear'],
        ['green_turban', 'headgear']
    ],
    [
        ['crow_mask', 'face'],
        ['blue_sunglasses', 'face'],
        ['smoky_makeup', 'face']
    ],
    [
        ['yellow_hat', 'headgear'],
        ['blue_sunglasses', 'eyewear'],
        ['green_turban', 'headgear'],
        ['crow_mask', 'face'],
        ['blue_sunglasses', 'face'],
        ['smoky_makeup', 'face']
    ],
    [
        ['yellow_hat', 'headgear'],
    ]
]

for c in cases:
    s = solution(c)
    print(s)
