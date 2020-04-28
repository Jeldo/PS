'''
Category: Dynamic Programming
'''


class Solution:
    def minCostClimbingStairs(self, cost: list):
        c = [0 for _ in range(0, len(cost)+1)]
        c[0], c[1] = cost[0], cost[1]
        for i in range(2, len(cost) + 1):
            c[i] = min(c[i-1], c[i-2]) + (0 if i == len(cost) else cost[i])
        return c[len(cost)]


cases = [
    [10, 15, 20],
    [1, 100, 1, 1, 1, 100, 1, 1, 100, 1],
    [0, 1, 2, 3]
]

for c in cases:
    s = Solution().minCostClimbingStairs(c)
    print(s)
