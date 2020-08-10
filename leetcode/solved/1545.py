class Solution:
    def findKthBit(self, n: int, k: int):
        dp = ['0']

        def reverse_and_invert(s):
            temp = s + '1'
            for ch in reversed(s):
                if ch == '0':
                    temp += '1'
                else:
                    temp += '0'
            return temp
        for i in range(1, n):
            dp.append(reverse_and_invert(dp[i-1]))
        return dp[-1][k-1]


cases = [
    [3, 1],
    [4, 11],
    [1, 1],
    [2, 3]
]

for c in cases:
    s = Solution().findKthBit(c[0], c[1])
    print(s)
