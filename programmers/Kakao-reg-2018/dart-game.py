def solution(dartResult):
    score = [0, 0, 0]
    numbers = set('0123456789')
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = set('*#')
    time = -1
    cur = ''
    for char in dartResult:
        if char in numbers:
            cur += char
        elif char in bonus:
            score[time+1] = int(cur) ** bonus[char]
            cur = ''
            time += 1
        elif char in option:
            if char == '*':
                score[time] *= 2
                if 0 <= time - 1:
                    score[time-1] *= 2
            elif char == '#':
                score[time] *= -1
    return sum(score)


cases = [
    '1S2D*3T',
    '1D2S#10S',
    '1D2S0T',
    '1S*2T*3S',
    '1D#2S*3S',
    '1T2D3D#',
    '1D2S3T*',
]

for c in cases:
    s = solution(c)
    print(s)
