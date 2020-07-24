'''
Category: Stack
Time Complexity: O(n)
'''


class Solution:
    def nextGreaterElements(self, nums):
        stack, res = [], [-1] * len(nums)
        for _ in range(2):
            for i in range(len(nums)):
                while stack and nums[stack[-1]] < nums[i]:
                    res[stack.pop()] = nums[i]
                    print(i, stack, res)
                stack.append(i)
                print(i, stack, res)
        return res


cases = [
    [1, 2, 1],  # 2 -1 2
    [3, 1, 2]   # -1 3 3
]

for c in cases:
    s = Solution().nextGreaterElements(c)
    print(s)
