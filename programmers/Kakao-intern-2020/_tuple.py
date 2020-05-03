def solution(s):
    answer = []
    s= s[1:-1]
    temp = ''
    sets = list()
    i = 0
    while i < len(s):
        if s[i] == '{':
            i += 1
            while s[i] != '}':
                temp += s[i]
                i += 1
            temp = [int(x) for x in temp.split(',')]
            sets.append(temp)
            temp = ''
        i += 1
    sets = sorted(sets, key=len)

    answer.extend(sets[0])
    for i in range(0, len(sets)-1):
        num = list(set(sets[i+1])-set(sets[i]))[0]
        answer.append(num)
    return answer

cases = [
    "{{2},{2,1},{2,1,3},{2,1,3,4}}",
    "{{1,2,3},{2,1},{1,2,4,3},{2}}",
    "{{20,111},{111}}",
    "{{123}}",
    "{{4,2,3},{3},{2,3,4,1},{2,3}}"	
]

for c in cases:
    s = solution(c)
    print(s)