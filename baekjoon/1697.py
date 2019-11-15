import sys
from collections import deque

def bfs(position, target):
    global MAX
    q = deque()
    q.append(position)
    while q:
        position = q.popleft()
        if position == target:
            return
        for next_step in (position-1, position+1, position*2):
            if 0 <= next_step < MAX and not counts[next_step]:
                print(counts[next_step])
                counts[next_step] = counts[position] + 1
                q.append(next_step)


MAX = 100001
args = sys.stdin.readline()
pos, target = map(int, args.split())
counts = [0] * MAX
bfs(pos, target)