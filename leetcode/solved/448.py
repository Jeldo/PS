class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums) + 1):
            n = nums[i - 1]
            while n != 0:
                next_n, nums[n - 1] = nums[n - 1], 0
                n = next_n

        return [i + 1 for i in range(len(nums)) if nums[i] != 0]

    def findDisappearedNumbers_abs(self, nums):
        for i in range(len(nums)):
            j = abs(nums[i]) - 1
            nums[j] = -abs(nums[j])
        return [i + 1 for i in range(0, len(nums)) if nums[i] > 0]


cases = [
    [4, 3, 2, 7, 8, 2, 3, 1],
    [1, 1],
    [1],
]

for c in cases:
    res = Solution().findDisappearedNumbers(c)
    print(res)
