class Solution:
    def findCircleNum(self, M: list):
        return 0


cases = [
    [
        [1, 1, 0],
        [1, 1, 0],
        [0, 0, 1]
    ],
    [
        [1, 1, 0],
        [1, 1, 1],
        [0, 1, 1]
    ]
]

for c in cases:
    s = Solution().findCircleNum(c)
    print(s)
