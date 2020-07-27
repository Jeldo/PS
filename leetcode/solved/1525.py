'''
Category: String
Time Complexity: O(n)
'''
from collections import Counter


class Solution:
    def numSplits(self, s: str):
        answer = 0
        left, right = {}, Counter(s)
        left_count, right_count = 0, len(Counter(s))
        for ch in s:
            if ch not in left.keys():
                left[ch] = 1
                left_count += 1
                right[ch] -= 1
                if right[ch] == 0:
                    right_count -= 1
            else:
                left[ch] += 1
                right[ch] -= 1
                if right[ch] == 0:
                    right_count -= 1
            if left_count == right_count:
                answer += 1
        return answer

    # brute force, time limit exceeded.
    def numSplits2(self, s: str):
        answer = 0
        for i in range(1, len(s)):
            left, right = Counter(s[:i]), Counter(s[i:])
            if len(left) == len(right):
                answer += 1
        return answer


cases = [
    "aacaba",
    "abcd",
    "aaaaa",
    "acbadbaada",
    "a",
    "ab",
    "aba"
]

for c in cases:
    s = Solution().numSplits(c)
    print(s)
