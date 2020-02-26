import math


class Solution:
    def fractionAddition(self, expression: str):
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

        divide = math.gcd(numsum, common_denominator)
        result = str(numsum//divide)+'/'+str(common_denominator//divide)

        # print(numerator_list)
        # print(denominator_list)
        # print(common_denominator)

        return result


# fractions = ["-1/2+1/2", "-1/2+1/2+1/3", "1/3-1/2", "5/3+1/3"]
# fractions = ["-1/2+1/2"]
fractions = ["-5/2+10/3+7/9"]
for f in fractions:
    s = Solution().fractionAddition(f)
    print(s)
