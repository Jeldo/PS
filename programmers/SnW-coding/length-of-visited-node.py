def solution(dirs):
    answer = 0
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    grid = [[0]*11 for _ in range(11)]
    pos = [5, 5]
    visited = set()
    for d in dirs:
        next_pos = None
        if d == 'U':
            next_pos = [pos[0]+dr[0], pos[1]+dc[0]]
        elif d == 'R':
            next_pos = [pos[0]+dr[1], pos[1]+dc[1]]
        elif d == 'D':
            next_pos = [pos[0]+dr[2], pos[1]+dc[2]]
        elif d == 'L':
            next_pos = [pos[0]+dr[3], pos[1]+dc[3]]
        if 0 <= next_pos[0] < 11 and 0 <= next_pos[1] < 11:
            if (tuple(pos), tuple(next_pos)) not in visited:
                visited.add((tuple(pos), tuple(next_pos)))
                visited.add((tuple(next_pos), tuple(pos)))
            pos = next_pos
    return len(visited)//2


cases = [
    'ULURRDLLU',
    'LULLLLLLU'
]


for c in cases:
    s = solution(c)
    print(s)
