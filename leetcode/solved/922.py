import queue


class Solution:
    def sortArrayByParityII(self, nums):
        even = list()
        odd = list()
        answer = list()
        for i in range(0, len(nums)):
            if nums[i] % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        total = len(even) + len(odd)

        for i in range(0, total):
            if i % 2 == 0:
                answer.append(even.pop())
            else:
                answer.append(odd.pop())
        return answer


ns = [4, 2, 5, 7]
sol = Solution()
print(sol.sortArrayByParityII(ns))
