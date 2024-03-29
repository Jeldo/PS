'''
Category: BFS
Time Complexity:
Space Complexity: O(n)
'''

from queue import Queue


class Solution:
    def canReach(self, arr, start):
        q = Queue()
        visited = [False] * len(arr)
        q.put([start, visited])
        while not q.empty():
            i, nums = q.get()
            isVisited = nums.copy()
            if arr[i] == 0:
                return True
            if isVisited[i]:
                continue
            isVisited[i] = True
            left, right = i - arr[i], i + arr[i]
            if 0 <= left < len(arr):
                q.put([left, isVisited])
            if 0 <= right < len(arr):
                q.put([right, isVisited])
        return False


# T T F T T F
cases = [
    [[4, 2, 3, 0, 3, 1, 2], 5],
    [[4, 2, 3, 0, 3, 1, 2], 0],
    [[3, 0, 2, 1, 2], 2],
    [[3, 0, 1, 2, ], 2],
    [[4, 4, 1, 3, 0, 3], 2],
    [[58, 48, 64, 36, 19, 19, 67, 13, 32, 2, 59, 50, 29, 68, 50, 0, 69, 31, 54, 20, 22, 43, 30, 9, 68, 71, 20, 22, 48, 74, 2, 65, 27, 54, 30, 5, 66, 24, 64,
        68, 9, 31, 50, 59, 15, 72, 6, 49, 11, 71, 12, 61, 5, 66, 30, 1, 2, 39, 59, 35, 53, 21, 76, 17, 71, 40, 68, 57, 64, 53, 70, 21, 50, 49, 25, 63, 35], 46]
]

for c in cases:
    s = Solution().canReach(c[0], c[1])
    print(s)
