import re


class Solution:
    def isPalindrome(self, s: str):
        new_s = ''
        for ch in s:
            if ch.isalnum():
                new_s += ch.lower()
        l, r = 0, len(new_s) - 1
        status = True
        while l < r:
            if new_s[l] != new_s[r]:
                status = False
                break
            l += 1
            r -= 1
        return status

    def isPalindrome2(self, s: str):
        s = re.sub('[^A-Za-z0-9]', '', s).lower()
        return s == s[::-1]


cases = [
    "A man, a plan, a canal: Panama",
    "race a car"
]

for c in cases:
    s = Solution().isPalindrome2(c)
    print(s)
