from itertools import combinations
import math


def solution(nums):
    def is_prime(n):
        if n % 2 == 0:
            return n == 2
        for i in range(3, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

    total = 0
    cm = combinations(nums, 3)
    for c in cm:
        if is_prime(sum(c)):
            print(c, sum(c))
            total += 1
    return total


cases = [
    [1, 2, 3, 4],
    [1, 2, 7, 6, 4]
]

for c in cases:
    s = solution(c)
    print(s)
