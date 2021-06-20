# O(NlogN)
def solution(A):
    nums = sorted(A)
    first = nums[-3] * nums[-2] * nums[-1]
    second = nums[0] * nums[1] * nums[-1]
    return max(first, second)


cases = [
    [-3, 1, 2, -2, 5, 6]
]

for c in cases:
    res = solution(c)
    print(res)
