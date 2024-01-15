from collections import Counter
from typing import List

# O(nlogn), n == len(matches)


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners, losers = Counter(), Counter()
        perfect_winners = []
        exact_defeated_once = []
        ONE_LOSS = 1

        for winner, loser in matches:
            winners[winner] += 1
            losers[loser] += 1

        for key in winners.keys():
            if key not in losers:
                perfect_winners.append(key)

        for k, v in losers.items():
            if v == ONE_LOSS:
                exact_defeated_once.append(k)

        perfect_winners.sort()
        exact_defeated_once.sort()

        return [perfect_winners, exact_defeated_once]


cases = [
    [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [
        4, 5], [4, 8], [4, 9], [10, 4], [10, 9]],
    [[2, 3], [1, 3], [5, 4], [6, 4]],
]

for c in cases:
    print(Solution().findWinners(c))
