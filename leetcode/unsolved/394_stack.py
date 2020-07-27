class Solution:
    def decodeString(self, s: str):
        stack = []
        temp = ''
        num = ''
        for i in range(0, len(s)):
            if s[i].isalpha():
                temp += s[i]
            elif s[i].isnumeric():
                if temp != '':
                    stack.append(temp)
                    temp = ''
                num += s[i]
            elif s[i] == '[':
                stack.append(num)
                num = ''
            elif s[i] == ']':
                prev = stack.pop()
                if prev.isalpha():
                    temp = prev + temp
                elif prev.isnumeric():
                    temp = temp * int(prev)
                stack.append(temp)
                temp = ''
        if temp:
            stack.append(temp)

        print(stack)
        word = ''
        while stack:
            top = stack.pop()
            if top.isalpha():
                word = top + word
            elif top.isnumeric():
                word = word * int(top)
        return word

        # if stack[0].isnumeric():
        #     answer = int(stack[0]) * ''.join(stack[1:])
        # else:
        #     answer = ''.join(stack)
        # return word


cases = [
    "3[a]2[bc]",
    "3[a2[c]]",
    "2[abc]3[cd]ef",
    "abc3[cd]xyz",
    "3[a]2[b4[F]c]",
    "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
]

for c in cases:
    s = Solution().decodeString(c)
    print(s)
