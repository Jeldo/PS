'''
Category: Dynamic Programming
Time Complexity: O(n)
Space Complexity: O(n) or O(1)
'''


class Solution:
    def climbStairs(self, n: int):
        if n == 1:
            return 1
        steps = [_ for _ in range(0, n + 1)]
        steps[1], steps[2] = 1, 2
        for i in range(3, n + 1):
            steps[i] = steps[i-1] + steps[i-2]
        return steps[n]

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
