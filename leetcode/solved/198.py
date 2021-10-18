class Solution:
    def rob(self, nums: List[int]) -> int:
        before_3, before_2 = 0, 0
        max_num = max(nums[:3])
        for i in range(2, len(nums)):
            if 0 <= i - 2:
                before_2 = nums[i - 2]
            if 0 <= i - 3:
                before_3 = nums[i - 3]
            nums[i] += max(before_2, before_3)
            max_num = max(max_num, nums[i])

        return max_num
