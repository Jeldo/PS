from itertools import accumulate


class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        def shift(char, i):
            return chr((ord(char) - ord('a') + i) % (ord('z') - ord('a') + 1) + ord('a'))

        result = ''
        shifts = list(map(lambda x: x % (ord('z') - ord('a') + 1), list(accumulate(shifts[::-1]))[::-1]))
        print(shifts)
        for ch, n in zip(s, shifts):
            result += shift(ch, n)

        return result


cases = [
    ["abc", [3, 5, 9]],
    ["aaa", [1, 2, 3]],
    ["bad", [10, 20, 30]],  # jyh"
    ["abcd", [3, 5, 9, 0]],
]

for c in cases:
    print(Solution().shiftingLetters(*c))
