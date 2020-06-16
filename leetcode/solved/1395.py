'''
Category: Array
Time Complexity: O(n^3)
'''

from itertools import combinations


class Solution:
    def numTeams(self, rating: list):
        count = 0
        n = len(rating)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        count += 1
        return count

    # using brute force, too slow
    def numTeams2(self, rating: list):
        if len(rating) < 3:
            return 0
        count = 0
        for c in combinations(rating, 3):
            is_ascending = True
            is_descending = True
            for i in range(0, 2):
                if c[i] > c[i+1]:
                    is_ascending = False
                if c[i] < c[i+1]:
                    is_descending = False
            if is_ascending:
                count += 1
            if is_descending:
                count += 1
        return count


# 3 0 4
cases = [
    [2, 5, 3, 4, 1],
    [2, 1, 3],
    [1, 2, 3, 4]
]

for c in cases:
    s = Solution().numTeams(c)
    print(s)
