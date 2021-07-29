from collections import deque


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        result = []
        intervals.sort()
        for interval in intervals:
            if not result or result[-1][1] < interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])

        return result

    def merge2(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        intervals = deque(intervals)
        start, end = intervals[0][0], intervals[0][1]
        result = []

        while intervals:
            if intervals[0][0] <= end:
                _, e = intervals.popleft()
                end = max(end, e)
            if not intervals:
                break
            if end < intervals[0][1]:
                result.append([start, end])
                start, end = intervals[0][0], intervals[0][1]
        if not result:
            result.append([start, end])
        if result[-1] != [start, end]:
            result.append([start, end])

        return result


cases = [
    [[1, 3], [2, 6], [8, 10], [15, 18]],
    [[1, 4], [4, 5]],
    [[1, 4], [0, 4]],
    [[1, 4], [2, 3]]
]

for c in cases:
    print(Solution().merge2(c))
