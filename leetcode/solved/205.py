# O(n)
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))

    def isIsomorphic_(self, s: str, t: str) -> bool:
        def patternize(string):
            pattern_map = dict()
            count = 0
            pattern = ""
            for ch in string:
                if ch in pattern_map:
                    pattern += str(pattern_map[ch])
                else:
                    count += 1
                    pattern_map[ch] = count
                    pattern += str(count)
            return pattern

        return patternize(s) == patternize(t)


cases = [
    ["egg", "add"],
    ["foo", "bar"],
    ["paper", "title"]
]

for c in cases:
    print(Solution().isIsomorphic(*c))
