class Solution:
    def myAtoi(self, s: str) -> int:
        min_range, max_range = -(2 ** 31), 2 ** 31 - 1
        s = s.lstrip()
        is_positive = None
        numbers = []
        for ch in s:
            if ch.isalpha() or ch == '.':
                break
            elif (numbers or is_positive) and not ch.isdigit():
                break
            elif ch == '+':
                if is_positive is None:
                    is_positive = True
                else:
                    return 0
            elif ch == '-':
                if is_positive is None:
                    is_positive = False
                else:
                    return 0
            elif ch.isdigit():
                numbers.append(ch)

        # join numbers if numbers exist
        num = ''.join(numbers)
        if not numbers:
            return 0

        # apply sign
        num = int(num)
        if is_positive is False:
            num = abs(num) * -1
        elif is_positive or is_positive is None:
            num = abs(num)

        # clamp
        if num < min_range:
            num = min_range
        elif num > max_range:
            num = max_range

        return num


cases = [
    "42",
    "-42",
    " 0042",
    " -0042",
    " 4193 with words",
    " -004193 with words",
    " 9999999999999999999999999",
    " -999999999999999999999999",
    "words and 987",  # 987
    "+-12",  # 0
    "00000-42a1234",  # 0
    "   +0 123",  # 0
    "  +  413",  # 0
]

for c in cases:
    print(Solution().myAtoi(c))
