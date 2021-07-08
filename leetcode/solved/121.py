import sys


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minimum_price = sys.maxsize
        profit = 0
        for price in prices:
            minimum_price = min(minimum_price, price)
            profit = max(profit, price - minimum_price)
        return profit


cases = [
    [7, 1, 5, 3, 6, 4],
    [7, 6, 4, 3, 1]
]

for c in cases:
    res = Solution().maxProfit(c)
    print(res)
