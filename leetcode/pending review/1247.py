'''
String
'''


class Solution:
    def minimumSwap(self, s1: str, s2: str):
        x_y, y_x = 0, 0
        count = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                if c1 == 'x':
                    x_y += 1
                else:
                    y_x += 1
        if (x_y + y_x) % 2 != 0:
            return -1
        count = x_y // 2
        count += y_x // 2
        if x_y % 2 != 0:
            count += 2
        return count


cases = [
    ['xx', 'yy'],
    ['xy', 'yx'],
    ['xx', 'xy'],
    ['xxyyxyxyxx', 'xyyxyxxxyx']
]

for c in cases:
    s = Solution().minimumSwap(*c)
    print(s)
