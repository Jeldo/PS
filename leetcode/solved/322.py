'''
Category: Dynamic Programming
Time Complexity: O(m*n), let m: len(coins), n: amount
Space Complexity: O(n)
'''

class Solution:
    def coinChange(self, coins: list, amount: int):
        c = [0 for _ in range(0, amount + 1)]
        for i in range(1, amount + 1):
            candidates = [c[i-coin]
                          for coin in coins if 0 <= i - coin and 0 <= c[i-coin]]
            if not candidates:
                c[i] = -1
            else:
                c[i] = min(candidates) + 1
        return c[amount] if 0 <= c[amount] else -1


cases = [
    [[1, 2, 5], 11],
    [[2], 3],
    [[1, 3, 5, 7], 23],
    [[1], 0],
    [[1, 5, 10, 21, 25], 63],
    [[2], 4],
    [[2, 3], 5],
]

for c in cases:
    s = Solution().coinChange(c[0], c[1])
    print(s)
    