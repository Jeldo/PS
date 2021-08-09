class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for ch in s:
            if ch.isalnum() or ch == '[':
                stack.append(ch)
            elif ch == ']':
                substring = ''
                repeat = ''
                while stack and stack[-1] != '[':
                    substring = stack.pop() + substring
                stack.pop()  # to remove '['
                while stack and stack[-1].isnumeric():
                    repeat = stack.pop() + repeat
                stack.append(int(repeat) * substring)
        return ''.join(stack)


cases = [
    "3[a]2[bc]",
    "3[a2[c]]",
    "2[abc]3[cd]ef",
    "abc3[cd]xyz",
]

for case in cases:
    print(Solution().decodeString(case))
