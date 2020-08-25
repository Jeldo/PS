class Solution:
    def maxSubArray(self, nums: list):
        max_so_far, cur_max = nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_max = max(nums[i], cur_max + nums[i])
            max_so_far = max(max_so_far, cur_max)
        return max_so_far

    # Kadane's Algorithm
    def maxSubArray1(self, nums: list):
        max_so_far, max_ending_here = 0, 0
        for i in range(len(nums)):
            max_ending_here += nums[i]
            if max_so_far < max_ending_here:
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far

    def maxSubArray2(self, nums: list):
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i-1] + nums[i])
        return max(nums)


cases = [
    [-2, 1, -3, 4, -1, 2, 1, -5, 4],
    [10, 1, -20, 5, 15, -30, 70]
]

for c in cases:
    s = Solution().maxSubArray(c)
    print(s)
