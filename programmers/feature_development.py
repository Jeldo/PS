def solution(progresses, speeds):
    distribution = list()
    while progresses:
        for i in range(0, len(progresses)):
            progresses[i] += speeds[i]
        count = 0
        while progresses:
            if progresses[0] >= 100:
                count += 1
                progresses.pop(0)
                speeds.pop(0)
            else:
                break
        if count > 0:
            distribution.append(count)
    return distribution

p = [93, 30, 55]
sp = [1, 30, 5]
# [2,1]
s = solution(p, sp)
print(s)