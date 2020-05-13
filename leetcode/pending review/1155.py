'''
Category: DP
'''


def show_table(table):
    for i in range(len(table)):
        for j in range(len(table[0])):
            print(table[i][j], end='\t')
        print()


class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int):
        dp = [[0 for i in range(target + 1)] for j in range(d + 1)]
        dp[0][0] = 1
        MOD = 10 ** 9 + 7
        for i in range(1, d + 1):
            for j in range(1, target + 1):
                k = 1
                while k <= min(j, f):
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - k]) % MOD
                    k += 1
        show_table(dp)
        return dp[d][target] % MOD


cases = [
    (1, 6, 3),  # 1
    (2, 6, 7),  # 6
    (2, 5, 10),  # 1
    (1, 2, 3),  # 0
    (3, 6, 6),  # 10
    (30, 30, 500)  # 222616187
]

for c in cases:
    s = Solution().numRollsToTarget(c[0], c[1], c[2])
    print(s)
