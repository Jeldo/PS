# O(n)
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        i = 0
        while i < len(nums):
            sub = [nums[i], nums[i+1], nums[i+2]]
            diff = max(sub) - min(sub)
            if k < diff:
                return []
            result.append(sub)
            i += 3
        return result
