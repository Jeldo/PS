'''
Category: String
'''
from collections import defaultdict
from collections import Counter


class Solution:
    def groupAnagrams(self, strs: list):
        d = defaultdict(list)
        for s in strs:
            d[tuple(sorted(s))].append(s)
        print(d)
        return [v for v in d.values()]

    def groupAnagrams2(self, strs: list):
        d = defaultdict(list)
        for s in strs:
            c = Counter(s)
            c = sorted(c.items(), key=lambda x: x[0])
            key = ''.join([x[0]*int(x[1]) for x in c])
            d[key].append(s)
        return [v for v in d.values()]


cases = [
    ["eat", "tea", "tan", "ate", "nat", "bat"],
    ["hos", "boo", "nay", "deb", "wow", "bop", "bob", "brr", "hey", "rye", "eve", "elf", "pup", "bum", "iva", "lyx", "yap", "ugh", "hem", "rod", "aha", "nam", "gap", "yea",
        "doc", "pen", "job", "dis", "max", "oho", "jed", "lye", "ram", "pup", "qua", "ugh", "mir", "nap", "deb", "hog", "let", "gym", "bye", "lon", "aft", "eel", "sol", "jab"]
]

for c in cases:
    s = Solution().groupAnagrams(c)
    print(s)
