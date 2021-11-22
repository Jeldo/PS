from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = sorted(zip(difficulty, profit))
        max_profit = 0
        max_of_each_worker = 0
        i = 0
        for ability in sorted(worker):
            while i < len(jobs) and jobs[i][0] <= ability:
                max_of_each_worker = max(jobs[i][1], max_of_each_worker)
                i += 1
            max_profit += max_of_each_worker
        return max_profit


cases = [
    [[2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]],
    [[85, 47, 57], [24, 66, 99], [40, 25, 25]],
    [[10, 20, 20, 30], [5, 10, 3, 20], [20, 21, 31, 9]]
]

for c in cases:
    print(Solution().maxProfitAssignment(*c))
