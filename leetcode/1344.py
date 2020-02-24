class Solution:
    def angleClock(self, hour: int, minutes: int):
        if hour == 12:
            hour = 0
        hour_angle = hour*30 + minutes * 0.5
        minutes_angle = minutes * 6
        ans = abs(hour_angle-minutes_angle)
        return 360 - ans if ans > 180 else ans


quiz = [(12, 30), (3, 30), (3, 15), (4, 50), (12, 0), (1, 57)]
for q in quiz:
    s = Solution().angleClock(q[0], q[1])
    print(s)
