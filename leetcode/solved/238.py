class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = []
        p = 1
        for i in range(len(nums)):
            result.append(p)
            p *= nums[i]
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= p
            p *= nums[i]
        return result

    def productExceptSelf2(self, nums):
        result = [1] * len(nums)
        left, right = 0, len(nums) - 1
        left_product = right_product = 1

        while left < len(nums):
            result[left] *= left_product
            result[right] *= right_product
            left_product *= nums[left]
            right_product *= nums[right]
            left += 1
            right -= 1

        return result


cases = [
    [1, 2, 3, 4],
    [-1, 1, 0, -3, 3]
]

for c in cases:
    res = Solution().productExceptSelf(c)
    print(res)
