class Solution:
    def findDisappearedNumbers(self, nums):
        for i in range(0, len(nums)):
            j = abs(nums[i])-1
            nums[j] = -abs(nums[j])
        return [i+1 for i in range(0, len(nums)) if nums[i] > 0]


nums = [4, 3, 2, 7, 8, 2, 3, 1]
s = Solution().findDisappearedNumbers(nums)
print(s)
