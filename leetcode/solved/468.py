class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        v4 = queryIP.split('.')
        v6 = queryIP.split(':')
        if len(v4) != 4 and len(v6) != 8:
            return 'Neither'

        # validate v4 ip
        if len(v4) == 4:
            converted_digits = []
            for digits in v4:
                if digits.isdigit():
                    converted_digit = int(digits)
                    if 0 <= converted_digit <= 255:
                        converted_digits.append(str(int(digits)))
                    else:
                        return 'Neither'
                else:
                    return 'Neither'

            new_v4 = '.'.join(converted_digits)
            if new_v4 == queryIP:
                return 'IPv4'
            return 'Neither'

        # validate v6 ip
        if len(v6) == 8:
            converted_digits = []
            for digits in v6:
                if len(digits) == 0 or len(digits) > 4:
                    return 'Neither'
                for ch in digits:
                    if ch.isalpha() and not ('a' <= ch.lower() <= 'f'):
                        return 'Neither'
                converted_digits.append(digits)

            new_v6 = ':'.join(converted_digits)
            origin_v6 = ':'.join(v6)
            if origin_v6 == new_v6:
                return 'IPv6'
            return 'Neither'


cases = [
    "172.16.254.1",  # v4
    "256.256.256.256",  # Neither
    "2001:0db8:85a3:0:0:8A2E:0370:7334",  # v6
    "2001:0db8:85a3:033:0:8A2E:0370:7334",  # v6
    "2001:db8:85a3:0::8a2E:0370:7334",  # Neither
    "20EE:FGb8:85a3:0:0:8A2E:0370:7334",  # Neither
    "2001:0db8:85a3::8A2E:037j:7334",  # Neither
    "02001:0db8:85a3:0000:0000:8a2e:0370:7334",  # Neither
]

for c in cases:
    print(Solution().validIPAddress(c))
