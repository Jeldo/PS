class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_integer = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        total = 0
        for i in range(len(s) - 1):
            current_num, next_num = roman_to_integer[s[i]], roman_to_integer[s[i + 1]]
            if current_num < next_num:
                total -= current_num
            else:
                total += current_num

        total += roman_to_integer[s[-1]]
        return total


cases = [
    "III", "LVIII", "MCMXCIV"
]

for c in cases:
    print(Solution().romanToInt(c))
