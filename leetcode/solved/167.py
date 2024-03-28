'''
Two Pointers
Time: O(n)
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        two_sum = numbers[l] + numbers[r]
        while two_sum != target:
            if two_sum < target:
                l += 1
            else:
                r -= 1
            two_sum = numbers[l] + numbers[r]
        return [l + 1, r + 1]


cases = [
    [[2, 7, 11, 15], 9],
    [[2, 3, 4], 6],
    [[-1, 0], -1]
]

for c in cases:
    s = Solution().twoSum(*c)
    print(s)
