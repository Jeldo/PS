'''
Category: Hash Table
'''


from collections import Counter, defaultdict


class Solution:
    def groupAnagrams(self, strs: list):
        dd = defaultdict(list)
        for s in strs:
            dd[''.join(sorted(s))].append(s)
        return list(dd.values())

    def groupAnagrams2(self, strs: list):
        dd = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch)-ord('a')] += 1
            dd[tuple(count)].append(s)
        return dd.values()


cases = [
    ["eat", "tea", "tan", "ate", "nat", "bat"],
]

for c in cases:
    s = Solution().groupAnagrams2(c)
    print(s)
