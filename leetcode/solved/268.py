class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        return sum(range(1, len(nums) + 1)) - sum(nums)

    # XOR -> 교환, 결합법칙이 성립
    # a ^ a = 0, a ^ 0 = a
    # [3, 0, 1] ^ [0, 1, 2, 3] => 2
    # XOR operation will remove duplicates
    def missingNumber2(self, nums: list[int]) -> int:
        missing = len(nums)
        for i, n in enumerate(nums):
            missing ^= i ^ n
        return missing


cases = [
    [3, 0, 1],
    [0, 1],
    [9, 6, 4, 2, 3, 5, 7, 0, 1],
    [0],
    [0, 1, 3, 4],
]

for c in cases:
    print(Solution().missingNumber2(c))
