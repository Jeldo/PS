class Solution:
    def restoreString(self, s: str, indices: list):
        chars = []
        for ch, i in zip(s, indices):
            chars.append((i, ch))
        chars = sorted(chars, key=lambda x: x[0])
        return ''.join([x[1] for x in chars])


cases = [
    ["codeleet",  [4, 5, 6, 7, 0, 2, 1, 3]],
    ["abc",  [0, 1, 2]],
    ["aiohn", [3, 1, 4, 2, 0]],
    ["aaiougrt",  [4, 0, 2, 6, 7, 3, 1, 5]],
    ["art", [1, 0, 2]]
]

for c in cases:
    s = Solution().restoreString(c[0], c[1])
    print(s)
