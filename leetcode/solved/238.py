from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1
        left_product, right_product = 1, 1
        product = [1] * len(nums)

        while left < len(nums):
            product[left] *= left_product
            product[right] *= right_product
            left_product *= nums[left]
            right_product *= nums[right]
            left += 1
            right -= 1

        return product


cases = [
    [1, 2, 3, 4],
    [-1, 1, 0, -3, 3],
]

for c in cases:
    print(Solution().productExceptSelf(c))
