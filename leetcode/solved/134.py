class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total, start = 0, 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                start = i + 1
        return start


cases = [
    [[1, 2, 3, 4, 5], [3, 4, 5, 1, 2]],
    [[2, 3, 4], [3, 4, 3]],
]

for c in cases:
    s = Solution().canCompleteCircuit(*c)
    print(s)
