'''
Category: Stack
Time Complexity: O(n**2)
'''


class Solution:
    def reverseParentheses(self, s):
        res = ['']
        for ch in s:
            if ch == '(':
                res.append('')
            elif ch == ')':
                temp = res.pop()[::-1]
                res[-1] += temp
            else:
                res[-1] += ch
            print(res)
        return ''.join(res)


cases = [
    "(abcd)",
    "(u(love)i)",
    "(ed(et(oc))el)",
    "a(bcdefghijkl(mno)p)q"
]

for c in cases:
    s = Solution().reverseParentheses(c)
    print(s)
