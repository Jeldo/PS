from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        if len(s) < 10:
            return []
        once = set()
        twice = set()
        for i in range(len(s) - 9):
            sequence = s[i:i + 10]
            if sequence in once:
                twice.add(sequence)
            else:
                once.add(sequence)
        return list(twice)

    def findRepeatedDnaSequences2(self, s: str) -> list[str]:
        if len(s) < 10:
            return []
        d = defaultdict(int)
        for i in range(len(s) - 9):
            d[s[i:i + 10]] += 1
        return [k for k, v in d.items() if v > 1]


cases = [
    "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",
    "AAAAAAAAAAAAA",
]

for c in cases:
    print(Solution().findRepeatedDnaSequences(c))
