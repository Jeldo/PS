class Solution:
    def reverseString(self, s):
        for i in range(0, int(len(s)/2)):
            temp = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = temp


sol = Solution()

word = ['h', 'e', 'l', 'l', 'o', '!']
print(word)
sol.reverseString(word)
print(word)
