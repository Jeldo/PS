class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        result = []
        prev_elements = []

        def dfs(elements):
            if not elements:
                result.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
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
