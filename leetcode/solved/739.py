'''
Category: Stack
Time Complexity: O(n)
'''


class Solution:
    def dailyTemperatures(self, T):
        days = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while len(stack) > 0 and stack[-1][1] < t:
                temp_i, _ = stack.pop()
                days[temp_i] = i - temp_i
            stack.append((i, t))
        return days


cases = [
    [73, 74, 75, 71, 69, 72, 76, 73]
]

for c in cases:
    s = Solution().dailyTemperatures(c)
    print(s)
