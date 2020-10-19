def solution(numbers, target):
    method = set()

    def dfs(i, arr):
        nonlocal method
        if i == len(arr):
            return
        positive = arr[:i] + [arr[i]] + arr[i+1:]
        negative = arr[:i] + [-arr[i]] + arr[i+1:]
        if sum(positive) == target:
            method.add(tuple(positive))
        if sum(negative) == target:
            method.add(tuple(negative))
        dfs(i+1, positive)
        dfs(i+1, negative)
    dfs(0, numbers)
    return len(method)


cases = [
    [[1, 1, 1, 1, 1], 3]
]

for c in cases:
    s = solution(*c)
    print(s)
