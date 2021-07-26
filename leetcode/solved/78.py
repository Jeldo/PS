class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def dfs(nums, path):
            result.append(path)
            for i in range(len(nums)):
                dfs(nums[i + 1:], path + [nums[i]])

        dfs(nums, [])
        return result


cases = [
    [1, 2, 3],
    [0],
]

for c in cases:
    print(Solution().subsets(c))
