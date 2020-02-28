import math


class Solution:
    def nthSuperUglyNumber(self, n, primes):
        num = 2
        primes = set(primes)
        ugly_numbers = set([1])

        def get_primes(number):
            primes = set()
            for i in range(2, int(math.sqrt(number))+1):
                while number % i == 0:
                    number //= i
                    if i not in primes:
                        primes.add(i)
            if number > 1:
                primes.add(number)
            return primes

        while len(ugly_numbers) < n:
            primes_of_ugly_number = get_primes(num)
            if len(primes_of_ugly_number-primes) == 0:
                ugly_numbers.add(num)
            num += 1
        # print(sorted(ugly_numbers))
        return max(ugly_numbers)


# n = 12
# primes = [2, 7, 13, 19]
# n = 700
# primes = [7, 11, 17, 23, 29, 31, 43, 47, 53, 67, 71, 73, 79, 89, 101, 113,
#           127, 131, 149, 151, 157, 163, 167, 179, 181, 199, 211, 223, 227, 251]
n = 850
primes = [7, 13, 29, 31, 37, 41, 43, 53, 59, 61, 71, 73, 79, 83, 89, 101,
          107, 109, 127, 131, 137, 149, 151, 157, 173, 227, 229, 233, 239, 257]
s = Solution().nthSuperUglyNumber(n, primes)
print(s)
