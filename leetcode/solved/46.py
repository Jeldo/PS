# https://leetcode.com/problems/permutations/discuss/18296/Simple-Python-solution-(DFS).
class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def dfs(nums, path, res):
            if not nums:
                res.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]], res)

        result = []
        dfs(nums, [], result)
        return result


cases = [
    [1, 2, 3],
    [0, 1],
    [1],
    [1, 2, 3, 4],
]

for c in cases:
    res = Solution().permute(c)
    print(res)
