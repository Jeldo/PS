class Solution:
    def bulbSwitch(self, n):
        isOn = [False] * n
        for i in range(1, n+1):
            for j in range(1, n+1):
                if j % i == 0:
                    isOn[j-1] = not isOn[j-1]
        return isOn.count(True)


ns = [3, 4, 5, 6, 7, 8]
# 1 2 2 2 2 2

for n in ns:
    s = Solution().bulbSwitch(n)
    print(s)
