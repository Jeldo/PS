class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        result = []
        for i in range(len(nums)):
            j = abs(nums[i]) - 1
            if nums[j] < 0:
                result.append(abs(nums[i]))
                continue
            nums[j] = -abs(nums[j])
        return result

    def findDuplicates_2(self, nums):
        ans = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                ans.append(abs(nums[i]))
            else:
                nums[index] *= -1
        return ans


nums = [
    [4, 3, 2, 7, 8, 2, 3, 1],
    [5, 4, 6, 7, 9, 3, 10, 9, 5, 6],
]
for n in nums:
    s = Solution().findDuplicates(n)
    print(s)
