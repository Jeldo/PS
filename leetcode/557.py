class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        rev = list()
        for word in words:
            rev.append(word[::-1])
        return ' '.join(rev)

sol = Solution()
print(sol.reverseWords('hello world!'))
