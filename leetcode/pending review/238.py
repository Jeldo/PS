class Solution:
    # O(n) time, O(n) space
    def productExceptSelf(self, nums):
        ans, left, right = [0] * len(nums), [0] * len(nums), [0] * len(nums)
        left[0] = 1
        right[len(nums)-1] = 1
        print([x for x in range(1, len(nums))])
        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i-1]
        # for i in range(len(nums)-2, -1, -1):
        for i in reversed(range(len(nums)-1)):
            right[i] = right[i+1]*nums[i+1]
        for i in range(len(nums)):
            ans[i] = left[i] * right[i]
        return ans

    # O(n) time, O(1) space
    def productExceptSelf1(self, nums):
        ans = [0]*len(nums)
        ans[0] = 1
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
        right = 1
        for i in reversed(range(len(nums))):
            ans[i] = ans[i]*right
            right *= nums[i]
        return ans

    # O(n^2) time limit exceeds

    def productExceptSelf2(self, nums):
        ans = list()
        for i in range(0, len(nums)):
            new = nums[:i] + nums[i+1:]
            product = 1
            for j in range(0, len(new)):
                product *= new[j]
            ans.append(product)
        return ans


ns = [
    [1, 2, 3, 4],
    [-1, 2, -2, 1]
]

for n in ns:
    # s = Solution().productExceptSelf(n)
    s = Solution().productExceptSelf1(n)
    print(s)
