# O(n)
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        max_rob = 0
        for i in range(len(nums)):
            if 3 <= i:
                nums[i] += max(nums[i-3], nums[i-2])
            elif 2 <= i:
                nums[i] += nums[i-2]
            max_rob = max(max_rob, nums[i])

        return max_rob


cases = [
    [1, 2, 3, 1],
    [2, 7, 9, 3, 1],
]

for c in cases:
    print(Solution().rob(c))
