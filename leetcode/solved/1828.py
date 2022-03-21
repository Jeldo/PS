from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        result = []
        for query in queries:
            count = 0
            for point in points:
                x, y, r = query
                a, b = point
                if (x - a) ** 2 + (y - b) ** 2 <= r ** 2:
                    count += 1

            result.append(count)

        return result


cases = [
    [[[1, 3], [3, 3], [5, 3], [2, 2]], [[2, 3, 1], [4, 3, 1], [1, 1, 2]]],
    [[[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]], [[1, 2, 2], [2, 2, 2], [4, 3, 2], [4, 3, 3]]]
]

for c in cases:
    print(Solution().countPoints(*c))
