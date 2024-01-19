# O(n)
class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [1, 2]
        for i in range(2, n):
            steps.append(steps[i - 2] + steps[i - 1])
        return steps[n-1]


cases = [
    1, 2, 3, 4, 5
]

for c in cases:
    print(Solution().climbStairs(c))
