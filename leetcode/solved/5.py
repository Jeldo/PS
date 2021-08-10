class Solution:
    # dp
    def longestPalindrome(self, s: str) -> str:
        longest_substring, max_length = s[0], 1
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True

        for left in range(len(s) - 1, -1, -1):
            for right in range(left + 1, len(s)):
                if s[left] == s[right]:
                    if right - left == 1 or dp[left + 1][right - 1]:
                        dp[left][right] = True
                        if max_length < right - left + 1:
                            max_length = right - left + 1
                            longest_substring = s[left:right + 1]

        return longest_substring

    # two pointers
    def longestPalindrome2(self, s: str) -> str:
        def palindrome(left, right):
            while 0 <= left and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        if len(s) < 2 or s == s[::-1]:
            return s
        longest_substring = ''
        # start index
        for i in range(len(s) - 1):
            even_substring = palindrome(i, i + 1)
            odd_substring = palindrome(i, i + 2)
            longest_substring = max(longest_substring, even_substring, odd_substring, key=len)
        return longest_substring


cases = [
    'babad',
    'cbbd',
    'a',
    'ac',
]

for c in cases:
    res = Solution().longestPalindrome(c)
    print(res)
