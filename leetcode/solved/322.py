'''
Category: Dynamic Programming
Time Complexity: O(m*n), let m: len(coins), n: amount
Space Complexity: O(n)
'''


class Solution:
    def coinChange(self, coins: list, amount: int):
        dp = [0] * (amount + 1)
        for i in range(1, amount + 1):
            cand = [dp[i-c] for c in coins if 0 <= i - c and 0 <= dp[i-c]]
            dp[i] = min(cand) + 1 if cand else -1
        return dp[amount] if 0 <= dp[amount] else -1


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
    s = Solution().coinChange(*c)
    print(s)
