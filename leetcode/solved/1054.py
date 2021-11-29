import heapq
from collections import Counter
from typing import List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        codes, rearranged = [], []

        for k, v in counter.items():
            codes.append((-v, k))
        heapq.heapify(codes)

        while codes:
            v_1, k_1 = heapq.heappop(codes)
            rearranged.append(k_1)
            if not codes:
                break
            v_2, k_2 = heapq.heappop(codes)
            rearranged.append(k_2)
            if v_1 < -1:
                heapq.heappush(codes, (v_1 + 1, k_1))
            if v_2 < -1:
                heapq.heappush(codes, (v_2 + 1, k_2))

        return rearranged


cases = [
    [1, 1, 1, 2, 2, 2],
    [1, 1, 1, 1, 2, 2, 3, 3],
    [1, 1, 1, 1, 2, 2, 2],
    [1, 1, 1, 1, 2, 2, 3],
]

for c in cases:
    print(Solution().rearrangeBarcodes(c))
