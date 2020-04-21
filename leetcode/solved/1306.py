'''
Category: BFS
Time Complexity:
Space Complexity: 
'''

from queue import Queue


class Solution:
    def canReach(self, arr, start):
        q = Queue()
        q.put(start)
        while not q.empty():
            i = q.get()
            if arr[i] == 0:
                return True
            left, right = i - arr[i], i + arr[i]
            if 0 <= left < len(arr):
                if left - arr[left] == i or left + arr[left] == i:
                    return False
                q.put(left)
            if 0 <= right < len(arr):
                if right - arr[right] == i or right + arr[right] == i:
                    return False
                q.put(right)
        return False


cases = [
    [[4, 2, 3, 0, 3, 1, 2], 5],
    [[4, 2, 3, 0, 3, 1, 2], 0],
    [[3, 0, 2, 1, 2], 2],
    [[3, 0, 1, 2, ], 2]
]

for c in cases:
    s = Solution().canReach(c[0], c[1])
    print('ans:', s)
