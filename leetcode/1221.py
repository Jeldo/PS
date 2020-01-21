class Solution:
    def balancedStringSplit(self, s):
        count = 0
        current = 0
        for ch in s:
            if ch == 'L':
                current += 1
            else:
                current -= 1
            if current == 0:
                count += 1
        return count


# 4 3 1 2
words = ["RLRRLLRLRL", "RLLLLRRRLR", "LLLLRRRR", "RLRRRLLRLL"]
for word in words:
    print('count', Solution().balancedStringSplit(word))
