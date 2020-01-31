class Solution:
    def decompressRLElist(self, nums: list):
        answer = list()
        for i in range(0, len(nums), 2):
            answer.extend([nums[i+1]]*nums[i])
        return answer


nums = [1, 2, 3, 4]
s = Solution().decompressRLElist(nums)
print(s)
