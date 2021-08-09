class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')

        return s


cases = [
    "3+2*2",
    " 3/2 ",
    " 3+5 / 2 ",
    "123",
]

for case in cases:
    print(Solution().calculate(case))
