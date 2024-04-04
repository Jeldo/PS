class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if 0 < m and nums[m] < nums[m - 1]:
                r = m - 1
            elif m < len(nums) - 1 and nums[m] < nums[m + 1]:
                l = m + 1
            else:
                return m


cases = [
    [1, 2, 3, 1],
    [1, 2, 1, 3, 5, 6, 4]
]

for c in cases:
    print(Solution().findPeakElement(c))
