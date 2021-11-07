from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0
        while l <= r:
            if l == r:
                boats += 1
                break
            if people[r] == limit:
                boats += 1
                r -= 1
            elif people[l] + people[r] <= limit:
                boats += 1
                l += 1
                r -= 1
            elif people[l] + people[r] > limit:
                boats += 1
                r -= 1

        return boats


cases = [
    [[1, 2], 3],
    [[3, 2, 2, 1], 3],
    [[3, 5, 3, 4], 5],
    [[2, 4, 3, 5, 3], 5],
    [[2, 2], 6]
]

for c in cases:
    print(Solution().numRescueBoats(*c))
