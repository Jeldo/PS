'''
Category: DP
'''


class Solution:
    def minCostClimbingStairs(self, cost: list):
        dp = cost + [0]
        for i in range(2, len(cost)+1):
            dp[i] += min(dp[i-1], dp[i-2])
        return dp[-1]


cases = [
    [10, 15, 20],
    [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
]

for c in cases:
    s = Solution().minCostClimbingStairs(c)
    print(s)
