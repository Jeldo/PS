'''
since string concatenation is slow in python,
use list and join them
'''


class Solution:
    def reverseOnlyLetters(self, S):
        answer = list()
        right = len(S)-1
        for left_char in S:
            if left_char.isalpha():
                while not S[right].isalpha():
                    right -= 1
                answer.append(S[right])
                right -= 1
            else:
                answer.append(left_char)
        return ''.join(answer)

    def reverseOnlyLetters2(self, S):
        S = list(S)
        left, right = 0, len(S) - 1
        while left < right:
            if not S[left].isalpha():
                left += 1
            elif not S[right].isalpha():
                right -= 1
            else:
                S[left], S[right] = S[right], S[left]
                left += 1
                right -= 1
        return ''.join(S)


S = "a-bC-dEf-ghIj----e----"
s = Solution().reverseOnlyLetters2(S)
print(s)
