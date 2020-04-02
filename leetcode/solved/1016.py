'''
Category: String
Time Complexity: ?
'''


class Solution:
    def queryString(self, S, N):
        # for i in range(1, N+1):
        # to reduce range
        for i in range(N, N//2, -1):
            binary = bin(i)
            if str(binary)[2:] not in S:
                return False
        return True


cases = [
    ["0110", 3],
    ["0110", 4]
]

for c in cases:
    s = Solution().queryString(c[0], c[1])
    print(s)
