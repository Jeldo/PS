from itertools import permutations
import math


def solution(s):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True

    primes = set()
    for n in s:
        if is_prime(int(n)):
            primes.add(int(n))
    for i in range(len(s)):
        for p in permutations(s, i+1):
            num = ''.join(p)
            for j in range(len(num)):
                if num[j] != '0':
                    n = int(num[j:])
                    if is_prime(n):
                        primes.add(n)
                    break
    return len(primes)


cases = [
    '17',
    '011',
    '317',
    '001101',
    '1234'
]

for c in cases:
    s = solution(c)
    print(s)
