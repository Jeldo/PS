import heapq


def solution(scoville, K):
    time = 0
    heapq.heapify(scoville)
    while len(scoville) >= 2 and scoville[0] < K:
        time += 1
        f = heapq.heappop(scoville)
        s = heapq.heappop(scoville)
        heapq.heappush(scoville, f + s * 2)
    return time if scoville[0] >= K else -1


cases = [
    [[1, 2, 3, 9, 10, 12], 7],
    [[1, 2], 100]
]

for c in cases:
    s = solution(*c)
    print(s)
