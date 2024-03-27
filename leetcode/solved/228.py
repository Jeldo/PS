class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        intervals = []
        interval = []
        for n in nums:
            if interval and interval[-1] + 1 == n:
                interval.append(n)
            else:
                if interval:
                    intervals.append(interval)
                interval = [n]
        if interval:
            intervals.append(interval)

        result = []
        for intv in intervals:
            if len(intv) == 1:
                result.append(str(intv[0]))
            else:
                result.append(f"{intv[0]}->{intv[-1]}")
        return result
