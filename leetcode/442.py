class Solution:
    def findDuplicates(self, nums):
        ans = list()
        for i in range(0, len(nums)):
            index = abs(nums[i])-1
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
