class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        result = []

        def dfs(nums, path):
            path_sum = sum(path)
            if path_sum == target:
                result.append(path)
                return
            elif path_sum > target:
                return
            elif path_sum < target:
                for i in range(len(nums)):
                    dfs(nums[i:], path + [nums[i]])

        dfs(candidates, [])
        return result


cases = [
    [[7, 3, 2, 6], 7],
    [[2, 3, 5], 8],
    [[2], 1],
    [[1], 1],
]

for c in cases:
    res = Solution().combinationSum(*c)
    print(res)
