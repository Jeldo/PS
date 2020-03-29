class Solution:
    def arrayPairSum(self, nums):
        n = sorted(nums)
        sum = 0
        for i in range(0, len(nums)):
            if i % 2 == 0:
                sum += n[i]
        return sum


ins = [1, 4, 3, 2, 5, 6]
sol = Solution()
print(sol.arrayPairSum(ins))
