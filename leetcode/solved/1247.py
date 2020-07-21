'''
Category: String

'''
from collections import Counter


class Solution:
    def minimumSwap(self, s1: str, s2: str):
        for i, ch in enumerate(zip(s1, s2)):
            if ch[0] == ch[1]:
                s1 = s1[:i] + s1[i+1:]
                s2 = s2[:i] + s2[i+1:]
        c1, c2 = Counter(s1), Counter(s2)
        if (c1['x'] + c2['x']) % 2 != 0 or (c1['y'] + c2['y']) % 2 != 0:
            return False
        print(s1, s2)
        print(c1, c2)
        return True


cases = [
    ["xx", "yy"],
    ["xy", "yx"],
    ["xx", "xy"],
    ["xxyyxyxyxx", "xyyxyxxxyx"],
    ["xyxyxyx", "yxyxxxy"]
]

for c in cases:
    s = Solution().minimumSwap(c[0], c[1])
    print(s)
