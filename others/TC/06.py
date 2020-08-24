data = '0 0 0 0;0 1 1 0;0 0 1 0;0 0 0 0'

data = data.split(';')
room = []
for d in data:
    room.append([int(r) for r in d.split()])
count = 0
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
for i in range(len(room)):
    for j in range(len(room[0])):
        if room[i][j] == 1:
            for r, c in zip(dr, dc):
                if room[i+r][j+c] == 0:
                    print((i, j), (i+r, j+c))
                    count += 1
print(count)
print(room)
