class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        duplicates = []
        for n in nums:
            if nums[abs(n)-1] < 0:
                duplicates.append(abs(n))
                continue
            nums[abs(n)-1] = -nums[abs(n)-1]
        return duplicates


nums = [
    [4, 3, 2, 7, 8, 2, 3, 1],
    [5, 4, 6, 7, 9, 3, 10, 9, 5, 6],
]
for n in nums:
    s = Solution().findDuplicates(n)
    print(s)
