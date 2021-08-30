class Solution:
    def canJump(self, nums):
        last = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= last:
                last = i
        return last == 0


cases = [
    [2, 3, 1, 1, 4],
    [3, 2, 1, 0, 4],
    [1, 1, 1, 0, 1],
    [1, 1, 2, 0, 1],
    [4, 0, 0, 0, 1],
    [2, 0],
]

for c in cases:
    print(Solution().canJump(c))
