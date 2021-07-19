from collections import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = Counter(s), set(), []

        for ch in s:
            counter[ch] -= 1
            if ch in seen:
                continue
            while stack and ch < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(ch)
            seen.add(ch)

        return ''.join(stack)


cases = [
    "bcabc",  # abc
    "cbacdcbc",  # acdb
]

for c in cases:
    res = Solution().removeDuplicateLetters(c)
    print(res)
