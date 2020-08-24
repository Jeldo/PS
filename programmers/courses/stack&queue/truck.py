from collections import deque


def solution(bridge_length, weight, truck_weights):
    truck_weights = deque(truck_weights)
    time, total = 0, 0
    d = deque([0]*bridge_length)
    while True:
        time += 1
        if d:
            total -= d.popleft()
        if truck_weights and truck_weights[0] + total <= weight:
            total += truck_weights[0]
            d.append(truck_weights.popleft())
        else:
            d.append(0)
        if not truck_weights and total == 0:
            break
    return time


cases = [
    [2, 10, [7, 4, 5, 6]],
    [100, 100, [10]],
    [100, 100, [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]]
]

for c in cases:
    s = solution(*c)
    print(s)
