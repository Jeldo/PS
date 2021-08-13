import heapq
from collections import Counter


class Solution:
    def reorganizeString(self, s: str):
        result, prev = '', ''
        q = [(-v, k) for k, v in Counter(s).items()]
        heapq.heapify(q)
        while q:
            v1, k1 = heapq.heappop(q)
            if k1 == prev:
                return ''
            result += k1
            prev = k1
            if q:
                v2, k2 = heapq.heappop(q)
                if k2 == prev:
                    return ''
                result += k2
                prev = k2
                if v2 + 1 != 0:
                    heapq.heappush(q, (v2 + 1, k2))
            if v1 + 1 != 0:
                heapq.heappush(q, (v1 + 1, k1))

        return result

    def reorganizeString2(self, s: str) -> str:
        q = [(-v, k) for k, v in Counter(s).items()]
        heapq.heapify(q)
        res = ''
        while len(q) > 1:
            first = heapq.heappop(q)
            second = heapq.heappop(q)
            v1, k1 = first
            v2, k2 = second
            res += k1
            res += k2
            if v1 + 1 < 0:
                heapq.heappush(q, (v1 + 1, k1))
            if v2 + 1 < 0:
                heapq.heappush(q, (v2 + 1, k2))
        if q:
            v, k = q.pop()
            res += k * -v
        prev = ''
        for ch in res:
            if prev == ch:
                return ''
            prev = ch
        return res


cases = [
    'aab',
    'aaab',
    'aaaabbb',
]

for c in cases:
    print(Solution().reorganizeString(c))
