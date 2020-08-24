def solution(prices):
    price = [0] * len(prices)
    stack = []

    for i, p in enumerate(prices):
        while stack and stack[-1][0] > p:
            temp = stack.pop()
            price[temp[1]] = i - temp[1]
        stack.append((p, i))
    while stack:
        temp = stack.pop()
        price[temp[1]] = len(prices) - temp[1] - 1
    return price


cases = [
    [1, 2, 3, 2, 3],
    [4, 5, 1, 3, 2, 5]
]

for c in cases:
    s = solution(c)
    print(s)
