class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        max_length = 0
        nums_set = set(nums)
        for n in nums_set:
            if n - 1 not in nums_set:
                length = 0
                while n + length in nums_set:
                    length += 1
                    max_length = max(max_length, length)

        return max_length


cases = [
    [100, 4, 200, 1, 3, 2],
    [0, 3, 7, 2, 5, 8, 4, 6, 0, 1],
    [0]
]

for c in cases:
    print(Solution().longestConsecutive(c))
