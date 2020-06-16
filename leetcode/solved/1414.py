'''
Category: Array
'''


class Solution:
    def findMinFibonacciNumbers(self, k: int):
        fibo = [1, 1]
        i = 2
        while True:
            next_num = fibo[i-2] + fibo[i-1]
            fibo.append(next_num)
            if next_num >= k:
                break
            i += 1
        total = 0
        count = 0
        for n in reversed(fibo):
            if total + n <= k:
                total += n
                count += 1
        return count


# 2 2 3 1
cases = [
    7, 10, 19, 3
]

for c in cases:
    s = Solution().findMinFibonacciNumbers(c)
    print(s)
