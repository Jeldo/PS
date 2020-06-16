'''
Category: Array
Time Complexity: O(n)
'''


class Solution:
    def kLengthApart(self, nums: list, k):
        distance = k
        for n in nums:
            if n == 0:
                distance += 1
            elif n == 1 and distance < k:
                return False
            else:
                distance = 0
        return True

    def kLengthApart2(self, nums: list, k: int):
        is_valid = True
        i = 0
        while i < len(nums):
            cur = nums[i]
            if cur == 1:
                break
            i += 1
        is_counting = False
        count = 0
        while i < len(nums):
            if not is_counting:
                is_counting = True
                i += 1
                continue
            cur = nums[i]
            if cur == 0:
                count += 1
            if cur == 1 and count < k:
                is_valid = False
                break
            if cur == 1 and count >= k:
                count = 0
            i += 1
        return is_valid


# T F T T T
cases = [
    [[1, 0, 0, 0, 1, 0, 0, 1], 2],
    [[1, 0, 0, 1, 0, 1], 2],
    [[1, 1, 1, 1, 1], 0],
    [[0, 1, 0, 1], 1],
    [[0, 0, 0, 0], 2],
    [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1], 4]
]

for c in cases:
    s = Solution().kLengthApart(c[0], c[1])
    print(s)
