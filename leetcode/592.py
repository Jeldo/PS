import math
import re
from fractions import Fraction


class Solution:
    # using re with fraction module
    def fractionAddition(self, expression: str):
        numbers = re.compile('[-+]').split(expression)
        total = sum([Fraction(x) for x in numbers if x])
        return '{}/{}'.format(total.numerator, total.denominator)

    # using re without fraction module
    def fractionAddition2(self, expression: str):
        numerator_list = list()
        denominator_list = list()
        numbers = re.compile('[-+]').split(expression)
        numbers = [x for x in numbers if x]
        for n in numbers:
            fraction = n.split('/')
            numerator_list.append(int(fraction[0]))
            denominator_list.append(int(fraction[1]))

        def lcm(x, y):
            return x*y // math.gcd(x, y)

        common_denominator = 1
        for i in range(0, len(denominator_list)):
            common_denominator = lcm(
                common_denominator, denominator_list[i])

        sum_of_denominators = 0
        for i in range(len(numerator_list)):
            multiply = common_denominator // denominator_list[i]
            sum_of_denominators += numerator_list[i] * multiply

        divisor = math.gcd(sum_of_denominators, common_denominator)
        result = str(sum_of_denominators//divisor) + \
            '/'+str(common_denominator//divisor)
        return result

    def fractionAddition3(self, expression: str):
        numerator_list = list()
        denominator_list = list()
        temp_string = str()
        is_numerator = True
        for ch in expression:
            if ch == '/' or ch == '+' or ch == '-' and len(temp_string) > 0:
                if is_numerator:
                    numerator_list.append(int(temp_string))
                    temp_string = ''
                else:
                    denominator_list.append(int(temp_string))
                    temp_string = ''
                is_numerator = not is_numerator
            if ch != '/':
                temp_string += ch
        denominator_list.append(int(temp_string))

        def lcm(x, y):
            return x*y // math.gcd(x, y)
        common_denominator = 1
        for i in range(0, len(denominator_list)):
            common_denominator = lcm(
                common_denominator, denominator_list[i])

        numsum = 0
        for i in range(len(numerator_list)):
            multiply = common_denominator // denominator_list[i]
            numsum += numerator_list[i] * multiply

        divisor = math.gcd(numsum, common_denominator)
        result = str(numsum//divisor)+'/'+str(common_denominator//divisor)

        return result


fractions = ["-1/2+1/2", "-1/2+1/2+1/3", "1/3-1/2", "5/3+1/3"]
for f in fractions:
    s = Solution().fractionAddition(f)
    print(s)
