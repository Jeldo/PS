class Solution:
    # Time: O(n), Space: O(1)
    def numTimesAllBlue(self, light):
        moments = 0
        right_most = 0
        for i in range(0, len(light)):
            bulb = light[i]
            right_most = max(bulb, right_most)
            print('i: {}, bulb: {}, rm: {}'.format(i, bulb, right_most))
            if i + 1 == right_most:  # all left bulbs are on
                print('moment')
                moments += 1
        return moments

    # Time limit exceed
    def numTimesAllBlue2(self, light):
        moments = 0
        isOn = [False] * len(light)
        right_most = 0
        for i in range(0, len(light)):
            idx = light[i] - 1
            right_most = max(idx, right_most)
            isOn[idx] = True
            if all(isOn[:right_most]):
                moments += 1
        return moments


lights = [
    [2, 1, 3, 5, 4],
    [3, 2, 4, 1, 5],
    [4, 1, 2, 3],
    [2, 1, 4, 3, 6, 5],
    [1, 2, 3, 4, 5, 6],
    [1, 3, 5, 7, 8, 6, 4, 2]
]
# 3 2 1 3 6
for light in lights:
    s = Solution().numTimesAllBlue(light)
    print(s)
