'''
Category: String
Time Complexity: O(n)
'''


class Solution:
    def minFlips(self, target: str):
        target = '0' + target
        count = 0
        prev = target[-1]
        for i in (range(len(target)-1, -1, -1)):
            if target[i] != prev:
                target = target[:i] + (len(target) - i) * target[i]
                count += 1
            prev = target[i]
        return count


cases = [
    "10111",
    "101",
    "00000",
    "001011101",
]

for c in cases:
    s = Solution().minFlips(c)
    print(s)
