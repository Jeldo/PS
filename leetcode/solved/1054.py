import heapq
from collections import defaultdict
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        codes = defaultdict(int)
        for code in barcodes:
            codes[code] += 1

        heap = []
        for code, count in codes.items():
            heap.append((-count, code))
        heapq.heapify(heap)

        result = []
        while heap:
            first_count, first_code = heapq.heappop(heap)
            result.append(first_code)
            if not heap:
                break
            second_count, second_code = heapq.heappop(heap)
            result.append(second_code)
            if first_count + 1 < 0:
                heapq.heappush(heap, (first_count + 1, first_code))
            if second_count + 1 < 0:
                heapq.heappush(heap, (second_count + 1, second_code))

        return result


cases = [
    [1, 1, 1, 2, 2, 2],
    [1, 1, 1, 2, 2],
    [1, 1, 1, 1, 2, 2, 3, 3],
]

for c in cases:
    print(Solution().rearrangeBarcodes(c))
