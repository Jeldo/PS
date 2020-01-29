'''
Time Complexity: O(n)
'''


class Solution:
    def twoSum(self, nums, target):
        numMap = dict()
        for i in range(0, len(nums)):
            complement = target - nums[i]
            # O(1) since dict is implemented as hash tables
            if complement in numMap.keys():
                return [numMap[complement], i]
            numMap[nums[i]] = i


nums = [3, 3]
target = 6
s = Solution().twoSum(nums, target)
print(s)
