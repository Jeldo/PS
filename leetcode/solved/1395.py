'''
Category: Array
'''

from itertools import combinations


class Solution:
    def numTeams(self, rating: list) -> int:
        left_less, left_greater = 0, 0
        right_less, right_greater = 0, 0
        count = 0
        for j in range(len(rating)):
            for i in range(j):
                if rating[i] < rating[j]:
                    left_less += 1
                elif rating[i] > rating[j]:
                    left_greater += 1
            for k in range(j+1, len(rating)):
                if rating[j] < rating[k]:
                    right_greater += 1
                elif rating[j] > rating[k]:
                    right_less += 1
            count += left_less * right_greater + left_greater * right_less
            left_less = left_greater = right_less = right_greater = 0
        return count

    def numTeams1(self, rating: list):
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
