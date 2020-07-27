'''
Category: String
Time Complexity: O(n)
'''


from collections import Counter

   def minSteps(self, s: str, t: str):
        # subtraction between two Counter objects returns new Counter object
        res = sum([v for k, v in (Counter(t) - Counter(s)).items()])
        return res

    # Faster than first method because of avoiding constructing new Counter object.
    def minSteps2(self, s, t):
        ans = 0
        ss = Counter(s)
        tt = Counter(t)
        for key, value in ss.items():
            diff = value - tt[key]
            if diff > 0:
                ans += diff
        return ans

    # Without using library
    def minSteps3(self, s, t):
        def get_dict(string):
            new_dict = dict()
            for ch in string:
                if ch not in new_dict:
                    new_dict[ch] = 1
                else:
                    new_dict[ch] += 1
            return new_dict

        ss = get_dict(s)
        tt = get_dict(t)
        ans = 0
        for key, value in ss.items():
            if key in tt:
                diff = value - tt[key]
                if diff > 0:
                    ans += diff
            else:
                ans += value
        return ans


cases = [
    ["bab", "aba"],
    ["leetcode", "practice"],
    ["anagram", "mangaar"],
    ["xxyyzz", "xxyyzz"],
    ["friend", "family"],
    ["abcde", "fghij"]
]

for c in cases:
    s = Solution().minSteps3(c[0], c[1])
    print(s)
