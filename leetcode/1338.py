from collections import Counter


class Solution:
    def minSetSize(self, arr):
        nums = list()
        count = 0
        for num in sorted([(value, key) for key, value in Counter(arr).items()], reverse=True):
            count += num[0]
            nums.append(num[1])
            if count >= len(arr)/2:
                break
        return len(nums)

    def minSetSize2(self, arr):
        nums = list()
        count = 0
        n = len(arr)/2
        for num in sorted(Counter(arr).items(), key=(lambda x: x[1]), reverse=True):
            nums.append(num[0])
            count += num[1]
            if count >= n:
                break
        return len(nums)


# 2 1 1 1 5 5
arr = [
    [3, 3, 3, 3, 5, 5, 5, 2, 2, 7],
    [7, 7, 7, 7, 7, 7],
    [1, 9],
    [1000, 1000, 3, 7],
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    [9, 77, 63, 22, 92, 9, 14, 54, 8, 38, 18, 19, 38, 68, 58, 19],
]
for a in arr:
    s = Solution().minSetSize2(a)
    print(s)
