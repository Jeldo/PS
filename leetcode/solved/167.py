'''
Two Pointers
Time: O(n)
'''


class Solution:
    # two pointers
    def twoSum(self, numbers: list, target: int):
        l, r = 0, len(numbers) - 1
        result = []
        while l < r:
            total = numbers[l] + numbers[r]
            if total == target:
                result = [l + 1, r + 1]
                break
            elif total < target:
                l += 1
            else:
                r -= 1
        return result


cases = [
    [[2, 7, 11, 15], 9],
    [[2, 3, 4], 6],
    [[-1, 0], -1]
]

for c in cases:
    s = Solution().twoSum(*c)
    print(s)
