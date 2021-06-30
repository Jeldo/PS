class Solution:
    def trap(self, height: list[int]) -> int:
        if not height:
            return 0

        total = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[0], height[right]

        while left < right:
            left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
            if left_max <= right_max:
                total += left_max - height[left]
                left += 1
            else:
                total += right_max - height[right]
                right -= 1

        return total


cases = [
    [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
    [4, 2, 0, 3, 2, 5]
]

for c in cases:
    res = Solution().trap(c)
    print(res)
