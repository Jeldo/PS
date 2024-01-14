from collections import Counter

# O(n)


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        cond1 = set(word1) == set(word2)
        word1_values = Counter(word1).values()
        word2_values = Counter(word2).values()
        cond2 = Counter(word1_values) == Counter(word2_values)
        return cond1 and cond2


cases = [
    ["abc", "bca"],  # true
    ["a", "aa"],  # false
    ["cabbba", "abbccc"],  # true
    ["aaabbbbccddeeeeefffff", "aaaaabbcccdddeeeeffff"]  # false
]


for c in cases:
    print(Solution().closeStrings(*c))
