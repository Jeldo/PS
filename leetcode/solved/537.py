'''
Category: String
'''


class Solution:
    def complexNumberMultiply(self, a: str, b: str):
        a, b = a.split('+'), b.split('+')
        a_r, a_i, b_r, b_i = int(a[0]), int(
            a[1][:-1]), int(b[0]), int(b[1][:-1])
        real = a_r * b_r - a_i * b_i
        imaginary = a_i * b_r + a_r * b_i
        return str(real) + '+' + str(imaginary) + 'i'

    def complexNumberMultiply2(self, a, b):
        a1, a2 = map(int, a[:-1].split('+'))
        b1, b2 = map(int, b[:-1].split('+'))
        return '%d+%di' % (a1 * b1 - a2 * b2, a1 * b2 + a2 * b1)


cases = [
    ["1+1i", "1+1i"],   # "0+2i"
    ["1+-1i", "1+-1i"],  # "0+-2i"
]

for c in cases:
    s = Solution().complexNumberMultiply(c[0], c[1])
    print(s)
