class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        temp = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                temp.append(nums1[i])
                i += 1
            else:
                temp.append(nums2[j])
                j += 1
        while i < m:
            temp.append(nums1[i])
            i += 1
        while j < n:
            temp.append(nums2[j])
            j += 1
        for i in range(len(temp)):
            nums1[i] = temp[i]

        print(nums1)


cases = [
    [[1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3],
    [[1], 1, [], 0],
    [[0], 0, [1], 1],
]

for c in cases:
    Solution().merge(*c)
