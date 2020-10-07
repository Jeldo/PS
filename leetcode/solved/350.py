class Solution:
    def intersect(self, nums1, nums2):
        nums1, nums2 = sorted(nums1), sorted(nums2)
        if len(nums1) < len(nums2):
            return self.intersect(nums2, nums1)
        intersection = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                intersection.append(nums1[i])
                i += 1
                j += 1
        return intersection


cases = [
    [[1, 2, 2, 1], [2, 2]],
    [[4, 9, 5], [9, 4, 9, 8, 4]],
    [[1, 2], [1, 1]]
]

for c in cases:
    s = Solution().intersect(*c)
    print(s)
