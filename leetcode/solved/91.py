class Solution:
    def numDecodings(self, s: str) -> int:
        if s.startswith("0"):
            return 0
        decoder = set()
        for i in range(1, 27):
            decoder.add(f"{i}")
        dp = [0] * len(s)
        dp[0] = 1
        if len(s) >= 2:
            if s[0]+s[1] in decoder and s[1] in decoder:
                dp[1] = 2
            else:
                dp[1] = 1
        for i in range(2, len(s)):
            if s[i-1]+s[i] in decoder and s[i] in decoder:
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[-1]


cases = [
    "12",
    "226",
    "06",
    "13212",
    "12121",
    "1",
    "0",
    "9",
    "91",
    "10",
    "111",
    "101",
    "10101",
    "2101",
]

for c in cases:
    print(Solution().numDecodings(c))
