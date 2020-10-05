class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        l, r = 0, len(s) - 1
        vowels = 'aAeEiIoOuU'
        while l < r:
            while s[l] not in vowels and l < r:
                l += 1
            while s[r] not in vowels and l < r:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)


cases = [
    'hello',
    'leetcode',
    'aA'
]

for c in cases:
    s = Solution().reverseVowels(c)
    print(s)
