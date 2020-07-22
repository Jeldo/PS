'''
Category: Stack
Time Complexity: O(n)
'''

from queue import deque


class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        popped = deque(popped)
        for n in pushed:
            stack.append(n)
            while stack and popped and stack[-1] == popped[0]:
                stack.pop()
                popped.popleft()
        return len(popped) == 0


cases = [
    [[1, 2, 3, 4, 5], [4, 5, 3, 2, 1]],
    [[1, 2, 3, 4, 5], [4, 3, 5, 1, 2]]
]

for c in cases:
    s = Solution().validateStackSequences(c[0], c[1])
    print(s)
