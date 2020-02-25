import math


class Solution:
    def mirrorReflection(self, p: int, q: int):
        def get_lcm(a, b):
            return a*b//math.gcd(a, b)
        lcm = get_lcm(p, q)
        if p % q == 0:
            if p//q % 2 != 0:
                return 1
            else:
                return 2
        else:
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
            print('p:{}, q:{}'.format(p, q), p//q)
            s = Solution().mirrorReflection(p, q)
            print(s)
