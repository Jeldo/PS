class NumArray:

    def __init__(self, nums: list):
        self.dp = [0] + nums
        for i in range(1, len(nums)+1):
            self.dp[i] += self.dp[i-1]
        # for n in nums:
        #     self.dp.append(self.dp[-1] + n)

    def sumRange(self, i: int, j: int):
        return self.dp[j+1] - self.dp[i]


cases = [
    [-2, 0, 3, -5, 2, -1]
]

for c in cases:
    na = NumArray(c)
    s = na.sumRange(0, 2)
    print(s)
    s = na.sumRange(2, 5)
    print(s)
    s = na.sumRange(0, 5)
    print(s)
