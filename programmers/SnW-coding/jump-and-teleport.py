def solution(nums):
    count = 0
    while True:
        if nums == 0:
            return count
        nums, r = divmod(nums, 2)
        if r == 1:
            count += 1


cases = [
    5, 6, 5000
]

for c in cases:
    s = solution(c)
    print(s)
