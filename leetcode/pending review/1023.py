from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def match(query):
            p = 0
            for ch in query:
                if p < len(pattern) and pattern[p] == ch:
                    p += 1
                elif ch.isupper():
                    return False
            return p == len(pattern)

        result = []
        for q in queries:
            result.append(match(q))

        return result


cases = [
    [["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FB"],
    [["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FoBa"],
    [["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FoBaT"],
]

for c in cases:
    print(Solution().camelMatch(*c))
