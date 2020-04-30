'''
Category: Dynamic Programming
Time Complexity: O(n^2)
Space Complexity: O(1) - first solution, O(n^2) - second solution
'''


class Solution:
    # use original list input
    def minFallingPathSum(self, A: list):
        for i in range(1, len(A)):
            for j in range(0, len(A[0])):
                candidate = list()
                if 0 <= j - 1:
                    candidate.append(A[i-1][j-1])
                if j + 1 < len(A):
                    candidate.append(A[i-1][j+1])
                candidate.append(A[i-1][j])
                A[i][j] += min(candidate)
        return min(A[-1])
        
    # use new list to record a cost
    def minFallingPathSum2(self, A: list):
        cost = A.copy()
        for i in range(1, len(A)):
            for j in range(0, len(A[0])):
                candidate = list()
                if 0 <= j - 1:
                    candidate.append(A[i-1][j-1])
                if j + 1 < len(A):
                    candidate.append(A[i-1][j+1])
                candidate.append(A[i-1][j])
                cost[i][j] += min(candidate)
        return min(cost[-1])

    def minFallingPathSum3(self, A: list):
        for i in range(1, len(A)):
            for j in range(0, len(A[0])):
                min_cost = A[i-1][j]
                if 0 <= j - 1:
                    min_cost = min(min_cost, A[i-1][j-1])
                if j + 1 < len(A):
                    min_cost = min(min_cost, A[i-1][j+1])
                A[i][j] += min_cost
        return min(A[-1])


cases = [
    [[1,2,3],[4,5,6],[7,8,9]],
    [[-80,-13,22],[83,94,-5],[73,-48,61]],
    [[-10,0,10]]
]

for c in cases:
    s = Solution().minFallingPathSum3(c)
    print(s)
    