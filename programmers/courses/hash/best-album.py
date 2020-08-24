from collections import defaultdict
import heapq


def solution(genres, plays):
    answer = []
    genre_ranking = defaultdict(int)
    song_ranking = defaultdict(list)
    for i, (g, p) in enumerate(zip(genres, plays)):
        genre_ranking[g] += p
        heapq.heappush(song_ranking[g], (-p, i))
    genre_ranking = sorted(genre_ranking.items(),
                           key=lambda x: x[1], reverse=True)
    for g in genre_ranking:
        top_2 = heapq.nsmallest(2, song_ranking[g[0]])
        for r in top_2:
            answer.append(r[1])
    return answer


cases = [
    [['classic', 'pop', 'classic', 'classic', 'pop'],	[500, 600, 150, 800, 2500]]
]

for c in cases:
    s = solution(*c)
    print(s)
