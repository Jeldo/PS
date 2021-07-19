'''
Category: Stack
Time Complexity: O(n)
'''


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        days = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                temp = stack.pop()
                days[temp[1]] = i - temp[1]
            stack.append((t, i))
        return days


cases = [
    [73, 74, 75, 71, 69, 72, 76, 73],
    [30, 40, 50, 60],
    [30, 60, 90]
]

for c in cases:
    res = Solution().dailyTemperatures(c)
    print(res)
