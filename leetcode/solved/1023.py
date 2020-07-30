'''
Category: String
'''


class Solution:
    def camelMatch(self, queries: list, pattern: str):
        answer = []
        for q in queries:
            p = ''
            p_i = 0
            for ch in q:
                if ch.isupper():
                    p += ch
                    p_i += 1
                elif p_i < len(pattern):
                    if ch == pattern[p_i]:
                        p += ch
                        p_i += 1
            if p == pattern:
                answer.append(True)
            else:
                answer.append(False)
        return answer


cases = [
    [["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FB"],
    [["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FoBa"],
    [["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"], "FoBaT"]
]

for c in cases:
    s = Solution().camelMatch(c[0], c[1])
    print(s)
