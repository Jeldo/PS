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


cases = [
    [1, 2, 3, 4],
    [-1, 1, 0, -3, 3]
]

for c in cases:
    res = Solution().productExceptSelf(c)
    print(res)
