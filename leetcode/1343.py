'''
sub-array: continuous subset of original array
Time Complexity: O(n)

since using linear search and adding numbers causes timeout,
use integer object to contain sum of sub-array.
'''


class Solution:
    def numOfSubarrays(self, arr, k, threshold):
        total = sum(arr[:k])
        count = 0
        if total/k >= threshold:
            count += 1
        for i in range(k, len(arr)):
            total = total + arr[i] - arr[i-k]
            if total/k >= threshold:
                count += 1
        return count


q1 = [[2, 2, 2, 2, 5, 5, 5, 8], 3, 4]
q2 = [[1, 1, 1, 1, 1], 1, 0]
q3 = [[7, 7, 7, 7, 7, 7, 7], 7, 7]
q4 = [[11, 13, 17, 23, 29, 31, 7, 5, 2, 3], 3, 5]

s = Solution().numOfSubarrays(q1[0], q1[1], q1[2])
# s = Solution().numOfSubarrays(q2[0], q2[1], q2[2])
# s = Solution().numOfSubarrays(q3[0], q3[1], q3[2])
# s = Solution().numOfSubarrays(q4[0], q4[1], q4[2])
print(s)
