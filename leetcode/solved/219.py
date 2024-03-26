class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        duplicates = dict()
        for i, n in enumerate(nums):
            if n in duplicates:
                if abs(duplicates[n] - i) <= k:
                    return True
            duplicates[n] = i
        return False
