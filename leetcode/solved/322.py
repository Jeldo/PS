class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i-coin]+1)
        return dp[amount] if dp[amount] != amount+1 else -1


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
