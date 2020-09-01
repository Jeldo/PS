'''
Category: Dynamic Programming
Time Complexity: O(n)
Space Complexity: O(n) or O(1)
'''


class Solution:
    def climbStairs(self, n: int):
        cost = [1, 2] + [0] * (n - 2)
        if n == 1:
            return cost[0]
        elif n == 2:
            return cost[1]
        for i in range(2, n):
            cost[i] = cost[i-1] + cost[i-2]
        return cost[n-1]

    def climbStairs2(self, n: int):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        steps_1, steps_2 = 1, 2
        for i in range(3, n + 1):
            steps_1, steps_2 = steps_2, steps_1 + steps_2
        return steps_2


cases = [
    1, 2, 3, 4, 5
]

for c in cases:
    s = Solution().climbStairs2(c)
    print(s)
