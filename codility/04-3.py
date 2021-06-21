# O(n)
def solution(A):
    nums = set(range(1, len(A) + 1))
    for n in A:
        if n in nums:
            nums.remove(n)
    if not nums:
        return len(A) + 1
    return min(nums)


cases = [
    [1, 3, 6, 4, 1, 2],
    [1, 2, 3],
    [-1, -3],
    [-1],
    [2],
]

for c in cases:
    res = solution(c)
    print(res)
