class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        def dfs(nums, path):
            if len(path) == k:
                result.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[i + 1:], path + [nums[i]])

        result = []
        nums = list(range(1, n + 1))
        dfs(nums, [])

        return result


cases = [
    [4, 2],
    [1, 1],
]

for c in cases:
    res = Solution().combine(*c)
    print(res)
