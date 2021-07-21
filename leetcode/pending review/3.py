class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # key: character, value: index of character
        used = {}
        max_length = start = 0
        for i, ch in enumerate(s):
            if ch in used and start <= used[ch]:
                start = used[ch] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used[ch] = i
        return max_length


cases = [
    'abcabcbb',
    'bbbbb',
    'pwwkew',
    '',
]

for c in cases:
    res = Solution().lengthOfLongestSubstring(c)
    print(res)
