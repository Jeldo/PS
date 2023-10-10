from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i] = nums[index]
                index += 1
        return index


cases = [
    [[3, 2, 2, 3], 3],
    [[0, 1, 2, 2, 3, 0, 4, 2], 2],
]

for c in cases:
    print(Solution().removeElement(*c))
