'''
Category: String
Time Complexity: O(N*K), N=the number of words, K=the length of each word
'''


class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        def patternize(s):
            pattern_dict = {}
            p = 0
            result = ''
            for ch in s:
                if ch not in pattern_dict:
                    pattern_dict[ch] = str(p)
                    p += 1
                result += pattern_dict[ch]
            return result

        pattern_digit = patternize(pattern)
        return [word for word in words if pattern_digit == patternize(word)]


cases = [
    [["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"],
    [["a", "b", "c"], "a"],
]

for c in cases:
    print(Solution().findAndReplacePattern(*c))
