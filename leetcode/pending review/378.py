import heapq


class Solution:
    # O(n^2 logn) bruteforce
    def kthSmallest(self, matrix, k):
        heap_list = list()
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(heap_list, matrix[i][j])
        small = heapq.nsmallest(k, heap_list)[-1]
        return small

    # worst: O(nlogn)
    def kthSmallest2(self, matrix, k):
        min_heap = list()
        for i in range(min(k, len(matrix))):
            heapq.heappush(min_heap, (matrix[i][0], 0, matrix[i]))
        count, number = 0, 0
        while min_heap:
            number, i, row = heapq.heappop(min_heap)
            count += 1
            if count == k:
                break
            if len(row) > i+1:
                heapq.heappush(min_heap, (row[i+1], i+1, row))
        return number


matrix = [
    [1,  5,  9],  # top_row
    [10, 11, 14],
    [12, 13, 15]  # bottom_row
]
k = 8
s = Solution().kthSmallest2(matrix, k)
print(s)
