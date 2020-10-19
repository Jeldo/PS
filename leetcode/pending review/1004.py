'''
Time Complexity: O(n)
'''


class Solution:
    def longestOnes(self, A, K):
        i = 0
        for j in range(len(A)):
            K -= 1 - A[j]
            if K < 0:
                K += 1 - A[i]
                i += 1
        return len(A) - i

    def longestOnes1(self, A: list, K: int):
        total = 0
        l, r = 0, 0
        res = 0

        while r < len(A):
            if A[r] == 0:
                total += 1

            if total > K:
                while l < r and A[l] == 1:
                    l += 1
                total -= 1
                l += 1
            if (r - l + 1) > res:
                res = r - l + 1
            r += 1
        return res

    def longestOnes2(self, A: list, K: int):
        total = 0
        q = []
        start = 0
        for end in range(len(A)):
            print(start, end, total, q)
            if A[end] == 0:
                q.append(end)
            if q and len(q) > K:
                start = q.pop(0) + 1
            total = max(total, end - start + 1)
        return total


cases = [
    [[1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], 2],
    [[0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1],  3]
]

for c in cases:
    s = Solution().longestOnes2(*c)
    print(s)
