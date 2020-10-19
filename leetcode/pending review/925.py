'''
Two-pointers
'''


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        for t_i in range(len(typed)):
            if i < len(name) and name[i] == typed[t_i]:
                i += 1
            elif t_i == 0 or typed[t_i] != typed[t_i-1]:
                return False
        return i == len(name)


# T F T T F F T
cases = [
    ['alex', 'aaleex'],
    ["saeed", "ssaaedd"],
    ["leelee", "lleeelee"],
    ["laiden", "laiden"],
    ["alex", "aaleelx"],
    ['alex', 'alexxr'],
    ["vtkgn", "vttkgnn"]
]

for c in cases:
    s = Solution().isLongPressedName(*c)
    print(s)
