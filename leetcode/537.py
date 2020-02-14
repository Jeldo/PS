class Solution:
    def complexNumberMultiply(self, m, n):
        first = m.split('+')
        a = first[0]
        b = first[1].split('i')[0]
        second = n.split('+')
        c = second[0]
        d = second[1].split('i')[0]
        res = str(int(a)*int(c)-int(b)*int(d)) + \
            '+' + str(int(a)*int(d)+int(b)*int(c))+'i'
        return res


a = "1+-1i"
b = "1+-1i"
s = Solution().complexNumberMultiply(a, b)
print(s)
