'''
Category: DP
'''


class Solution:
    def mincostTickets(self, days: list, costs: list):
        print(days, costs)
        return


# 11 17
cases = [
    [[1, 4, 6, 7, 8, 20], [2, 7, 15]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15]]
]

for c in cases:
    s = Solution().mincostTickets(c[0], [1])
    print(s)
