import math


class Solution:
    def mirrorReflection(self, p: int, q: int):
        lcm = p*q//math.gcd(p, q)
        if lcm//q % 2 == 0:
            return 2
        else:
            if lcm//p % 2 == 0:
                return 0
            else:
                return 1


n = 7
for p in range(1, n):
    for q in range(1, n):
        if q <= p:
            s = Solution().mirrorReflection(p, q)
            print('p:{}, q:{}, s:{}'.format(p, q, s))
