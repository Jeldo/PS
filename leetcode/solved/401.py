from itertools import permutations


class Solution(object):
    def readBinaryWatch(self, n):
        def dfs(n, hours, mins, idx):
            if hours >= 12 or mins > 59:
                return
            if not n:
                res.append('{}:{:02d}'.format(hours, mins))
                return
            for i in range(idx, 10):
                if i < 4:   # 0~3 to check hours
                    dfs(n - 1, hours | (1 << i), mins, i + 1)
                else:       # 4~9 to check minutes
                    k = i - 4
                    dfs(n - 1, hours, mins | (1 << k), i + 1)

        res = []
        dfs(n, 0, 0, 0)
        return res


s = Solution().readBinaryWatch(2)
print(s)
