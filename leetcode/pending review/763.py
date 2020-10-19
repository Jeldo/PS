'''
Category: Two Pointers
Time Complexity: O(n)
'''


class Solution:
    def partitionLabels(self, S: str):
        res = []
        right_most = {ch: i for i, ch in enumerate(S)}
        l, r = 0, 0
        for i, ch in enumerate(S):
            r = max(r, right_most[ch])
            if i == r:
                res.append(i-l+1)
                l = i + 1
        return res


cases = [
    "ababcbacadefegdehijhklij"
]

for c in cases:
    s = Solution().partitionLabels(c)
    print(s)
