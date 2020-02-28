class Solution:
    def relativeSortArray(self, arr1, arr2):
        arr1_set = set(arr1)
        arr2_set = set(arr2)
        sub = list(sorted(arr1_set.difference(arr2_set), reverse=False))
        print(sub)

arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
sol = Solution()
print(sol.relativeSortArray(arr1, arr2))

# nope! duplicate will occur!